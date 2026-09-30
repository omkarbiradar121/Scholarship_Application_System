from functools import wraps
from flask import session, redirect, url_for


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapped_view


def role_required(role):
    def decorator(view):
        @wraps(view)
        def wrapped_view(*args, **kwargs):
            if "user_id" not in session:
                return redirect(url_for("auth.login"))

            if session.get("role") != role:
                if session.get("role") == "Student":
                    return redirect(url_for("dashboard.student_dashboard"))

                if session.get("role") == "Scholarship Officer":
                    return redirect(url_for("dashboard.admin_dashboard"))

                return redirect(url_for("auth.login"))

            return view(*args, **kwargs)

        return wrapped_view

    return decorator