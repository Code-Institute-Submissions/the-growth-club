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
    """Render Landing page"""
    return render_template('index.html')


# Resources List Functionality
@app.route("/get_resources")
def get_resources():
    # find resources in the the database
    resources = list(mongo.db.resources.find())
    # render the resources template
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
    session.pop("user")
    # return to log in page
    return redirect(url_for("login"))


# Add a Resource Functionality
@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    """Add Resource. First find the category and topic in the database then sort
    the them by the name key. Then pass the new variables over to the HTML
    template. """
    if request.method == "POST":
        # create dictionary for items in form
        resource = {
            "category_name": request.form.get("category_name"),
            "resource_name": request.form.get("resource_name"),
            "resource_description": request.form.get("resource_description"),
            "resource_date": request.form.get("resource_date"),
            "resource_link": request.form.get("resource_link"),
            "topic_name": request.form.get("topic_name"),
            "created_by": session["user"]
            }
        mongo.db.resources.insert_one(resource)
        flash("Resource Successfully Added")
        return redirect(url_for("get_resources"))
    # find category & topic in database
    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    # render the add_resources template
    return render_template("add_resource.html", categories=categories,
                           topics=topics)


@app.route("/edit_resource/<resource_id>", methods=["GET", "POST"])
def edit_resource(resource_id):
    """ Edit Resource. First, retrieve the resource from the database to be
    edited by using the id. Then the ID needs to be converted into a BSON
    data-type. Use the Post method to update the resource in the
    database."""
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "resource_name": request.form.get("resource_name"),
            "resource_description": request.form.get("resource_description"),
            "resource_date": request.form.get("resource_date"),
            "resource_link": request.form.get("resource_link"),
            "topic_name": request.form.get("topic_name"),
            "created_by": session["user"]
        }
        mongo.db.resources.update({"_id": ObjectId(resource_id)}, submit)
        flash("The resource was successfully edited and updated")
        # return to the resources page
        return redirect(url_for("get_resources"))
    # retrieve the resource from the database by id
    resource = mongo.db.resources.find_one({"_id": ObjectId(resource_id)})
    # find the category & topic from the database
    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    # render the edit_resources template
    return render_template("edit_resource.html", resource=resource,
                           categories=categories, topics=topics)


@app.route("/delete_resource/<resource_id>")
def delete_resource(resource_id):
    """Delete Resource. Find the resource by id and remove it from the
    database. The present a message to confirm that it has been deleted."""
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("The resource was successfully deleted")
    # return to the resources page
    return redirect(url_for("get_resources"))


@app.route("/get_categories")
def get_categories():
    """Get Categories from the database. Find the categories, then convert
    into a list and sort alphabetically by by the category_name. """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    # return the categories template
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ Add Category. If the function is called using the POST method, then
    the data from the form is retrieved, and inserted into the database.
    Otherwise it will display the empty form."""
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        # insert the category in the database
        mongo.db.categories.insert_one(category)
        flash("The new Category was Added")
        # return to the manage categories page
        return redirect(url_for("get_categories"))
    # return to the add_category page
    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ Edit Category. If the user submits an edit request, then the
    Category is retrieved from the database, updated in the database and after
    the user receives a message, they are taken back to the manage page. """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        # update the category in the database
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        # user returned to the categories page
        return redirect(url_for("get_categories"))
    # Using the category ID being sent into this function, the .find_one()
    # method is used on the categories collection
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update this to debug=False before submission
