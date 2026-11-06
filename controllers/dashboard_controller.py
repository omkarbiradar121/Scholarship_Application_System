from flask import Blueprint, render_template
from controllers.auth_helpers import admin_required, student_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/admin/dashboard")
@admin_required
def admin_dashboard():
    return render_template("admin_dashboard.html")


@dashboard_bp.route("/student/dashboard")
@student_required
def student_dashboard():
    return render_template("student_dashboard.html")
