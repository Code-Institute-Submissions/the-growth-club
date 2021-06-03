import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# setup an instance of PyMongo
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    """Landing page render"""
    return render_template('index.html')


@app.route("/get_resources")
def get_resources():
    resources = list(mongo.db.resources.find())
    return render_template("resources.html", resources=resources)


# Sign Up/Register Functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    """User Registration. Check if the username from the form element already
    exists within the Mongo database. If it does, then a message is sent to
    the user. If it does not exist then the new user is inserted in the
    dictionary."""
    # if the requested method is equal to "POST"
    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            # check if Mongo username matches input for username in form
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then give message
        if existing_user:
            flash("Username already exists")
            # take the user back to the sign up page
            return redirect(url_for("register"))

        # if no user is found, then insert data in the dictionary
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # to replace with modal
        flash("Registration successful! You can now view or share resources!")
        # take user to the profile page
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log In Functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    """User Log In. Check if the username from the form element already
    exists within the Mongo database. If it does, then the password is checked
    if it matches the user input. If the password matches then a success
    message is shown. If password does not match then message is shown and user
    is return to log in page. If username does not exist then message is shown
    to user and user is returned to the log in page."""
    # if the requested method is equal to "POST"
    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then check password
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    # if user password matches hashed password log in user
                    session["user"] = request.form.get("username").lower()
                    # if user password matches hashed password show message
                    flash("Hi, {}".format(request.form.get("username")))
                    # take user to the profile page
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if password does not match show message
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist show message
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile Functionality
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """User Profile. Find username in the database and retrieve the
    username. Then render the profile template with the user's name"""
    # find the user in the database
    username = mongo.db.users.find_one(
        # take the session user's username from Mongo
        {"username": session["user"]})["username"]

    # check if session['user'] cookie is truthy
    if session["user"]:
        # render appropriate profile template
        return render_template("profile.html", username=username)

    # return profile page with user's unique name
    return redirect(url_for("login"))

# Log out Functionality
@app.route("/logout")
def logout():
    """User Log Out. Send message to user, remove session and go back to the
    log in page."""
    # show message to user
    flash("You have been logged out")
    # remove user from session cookies
    session.pop("clear")
    # return to log in page
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update this to debug=False before submission
