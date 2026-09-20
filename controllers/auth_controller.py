from flask import Blueprint, render_template, request, flash

from models.user_model import get_user_by_email, create_student


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    student_id = request.form.get("student_id", "").strip()

    if not name or not email or not password or not student_id:
        flash("All fields are required.", "error")
        return render_template("register.html")

    if "@" not in email:
        flash("Please enter a valid email address.", "error")
        return render_template("register.html")

    existing_user = get_user_by_email(email)

    if existing_user:
        flash("Email already registered.", "error")
        return render_template("register.html")

    create_student(
        name,
        email,
        password,
        student_id
    )

    flash(
        "Registration successful. Please login to continue.",
        "success"
    )

    return render_template("register.html")