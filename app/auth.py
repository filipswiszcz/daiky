from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from .models.user import User
from . import memory

blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@blueprint.route("/sign-up", methods=("GET", "POST"))
def sign_up():
    if request.method == "POST":
        email, password, errors = request.form["email"], request.form["password"], []
        if not email: errors.append("You need to provide a valid email address.")
        if not password: errors.append("You need to provide a password (length: 16, at least one digit and one special character.")
        user = User(email, password)
        # add user to database
        memory.add_user(user)
    return render_template("auth/sign_up.html")