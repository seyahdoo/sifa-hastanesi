#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from db import *

from bson import json_util
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")
app.jinja_env.undefined = StrictUndefined

from raven.contrib.flask import Sentry
sentry = Sentry(app)


@app.route('/')
def index():
    """Homepage."""

    # look for user, if not user
    try:
        session["current_user"]["user_id"]
    except Exception as e:
        # go to login
        return redirect("/login")

    return redirect("/appointment")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    """Log user in if credentials provided are correct."""

    login_email = request.form.get("login_email")
    login_password = request.form.get("login_password")

    current_user = users.find_one({"email": login_email, "password": login_password})

    if current_user is None:
        flash("The email or password you have entered did not match our records. Please try again.", "danger")
        return redirect("/login")

    print(current_user)

    # Use a nested dictionary for session["current_user"] to store more than just user_id
    session["current_user"] = {
        "first_name": current_user["first_name"],
        "user_id": str(current_user["_id"]),
        "role": current_user["role"]
    }

    flash("Welcome {}. You have successfully logged in.".format(current_user["first_name"]), "success")

    return redirect("/")


@app.route("/logout")
def logout():
    """Log user out."""

    del session["current_user"]

    flash("Goodbye! You have successfully logged out.", "success")

    return redirect("/")


@app.route("/signup", methods=["GET"])
def show_signup():
    """Show signup form."""

    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    """Check if user exists in database, otherwise add user to database."""

    signup_email = request.form.get("signup_email")
    signup_password = request.form.get("signup_password")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    current_user = users.find_one({"email": signup_email})

    if current_user is None:
        new_user = {"email": signup_email,
                    "password": signup_password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": "patient"}
        new_user_id = users.insert_one(new_user).inserted_id

        # Add same info to session for new user as per /login route
        session["current_user"] = {
            "first_name": new_user["first_name"],
            "user_id": str(new_user_id)
        }

        flash("You have succesfully signed up for an account, and you are now logged in.", "success")
        return redirect("/")

    flash("An account already exists with this email address. Please login.", "danger")
    return redirect("/login")


@app.route("/appointment", methods=["GET"])
def appointment_see():
    """"See appointment dialog"""

    patients = list(users.find({"role": "patient"}))
    doctors = list(users.find({"role": "doctor"}))
    appointment_list = list(appointments.find())

    print(appointment_list)

    return render_template("appointment.html",
                           appointment_list=appointment_list,
                           patients=patients,
                           doctors=doctors)


@app.route("/appointment", methods=["POST"])
def appointment_grab():
    """Try to grab appointment."""

    date = request.form.get("appointment_date")
    time = request.form.get("appointment_time")

    #if (date, time) in appointments:

    #    flash("This appointment is taken!!! Unsuccessful!!!.", "danger")
    #    return redirect("/appointment")

    appointments.insert_one({"date": date, "time": time})
    flash("Successfully grabbed appointment. Congrats!!!", "success")

    return redirect("/appointment")


if __name__ == "__main__":
    app.debug = True

    PORT = int(os.environ.get("PORT", 8080))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="localhost", port=PORT, debug=DEBUG)
