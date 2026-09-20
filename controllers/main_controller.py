from flask import Blueprint, redirect, url_for


main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    return redirect(url_for("auth.register"))