from flask import Blueprint, render_template

from controllers.auth_helpers import admin_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin/scholarships")
@admin_required
def scholarships():
    return render_template(
        "admin_placeholder.html",
        page_id="admin-scholarships-page",
        page_title="Scholarships",
        active_page="scholarships",
    )


@admin_bp.route("/admin/application-requests")
@admin_required
def application_requests():
    return render_template(
        "admin_placeholder.html",
        page_id="admin-application-requests-page",
        page_title="Application Requests",
        active_page="application-requests",
    )


@admin_bp.route("/admin/scholarship-processing")
@admin_required
def scholarship_processing():
    return render_template(
        "admin_placeholder.html",
        page_id="admin-scholarship-processing-page",
        page_title="Scholarship Processing",
        active_page="scholarship-processing",
    )


@admin_bp.route("/admin/history")
@admin_required
def history():
    return render_template(
        "admin_placeholder.html",
        page_id="admin-history-page",
        page_title="History",
        active_page="history",
    )
