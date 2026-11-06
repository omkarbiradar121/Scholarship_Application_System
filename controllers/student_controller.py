from flask import Blueprint, render_template

from controllers.auth_helpers import student_required

student_bp = Blueprint("student", __name__)


@student_bp.route("/student/scholarships")
@student_required
def scholarships():
    return render_template(
        "student_placeholder.html",
        page_id="student-scholarships-page",
        page_title="Browse Scholarships",
        active_page="scholarships",
    )


@student_bp.route("/student/applications")
@student_required
def applications():
    return render_template(
        "student_placeholder.html",
        page_id="student-applications-page",
        page_title="My Applications",
        active_page="applications",
    )


@student_bp.route("/student/history")
@student_required
def history():
    return render_template(
        "student_placeholder.html",
        page_id="student-history-page",
        page_title="History",
        active_page="history",
    )
