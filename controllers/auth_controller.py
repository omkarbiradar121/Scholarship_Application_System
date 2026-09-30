from flask import Blueprint, render_template, request, flash, session, redirect, url_for

from models.user_model import get_user_by_email, create_student, authenticate_user

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

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        flash("Email and password are required.", "error")
        return render_template("login.html")

    user = authenticate_user(email, password)

    if not user:
        flash("Invalid email or password.", "error")
        return render_template("login.html")

    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["role"] = user["role"]

    if user["role"] == "Scholarship Officer":
        return redirect(url_for("dashboard.admin_dashboard"))

    return redirect(url_for("dashboard.student_dashboard"))



@auth.route("/logout", methods=["GET"])
def logout():
    session.clear()
    session.modified = True
    return redirect(url_for("auth.login"))