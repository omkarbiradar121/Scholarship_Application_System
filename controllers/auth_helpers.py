from functools import wraps

from flask import redirect, session, url_for


def is_logged_in():
    return "user_id" in session


def is_scholarship_officer():
    return session.get("role") == "Scholarship Officer"


def is_student():
    return session.get("role") == "Student"


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped_view


def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for("auth.login"))
        if is_student():
            return redirect(url_for("dashboard.student_dashboard"))
        if not is_scholarship_officer():
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped_view


def student_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for("auth.login"))
        if is_scholarship_officer():
            return redirect(url_for("dashboard.admin_dashboard"))
        if not is_student():
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped_view


def role_required(role):
    """Compatibility wrapper for existing routes while they migrate to named guards."""
    if role == "Scholarship Officer":
        return admin_required
    if role == "Student":
        return student_required
    raise ValueError(f"Unsupported role: {role}")
