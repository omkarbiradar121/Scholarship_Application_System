from flask import Blueprint, render_template
from controllers.auth_helpers import role_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/admin/dashboard")
@role_required("Scholarship Officer")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@dashboard_bp.route("/student/dashboard")
@role_required("Student")
def student_dashboard():
    return render_template("student_dashboard.html")