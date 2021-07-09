import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_sslify import SSLify
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
sslify = SSLify(app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# setup an instance of PyMongo
mongo = PyMongo(app)


# --- ADMIN USER FUNCTION --- #
def admin():
    """
    Set admin user
    """
    return session['user'] == 'admin'


# ------------------------------------------- #
#    USER: REGISTRATION | LOG IN | LOG OUT    #
# ------------------------------------------- #

# --- SIGN UP / REGISTER FUNCTIONALITY --- #
@app.route("/register", methods=["GET", "POST"])
def register():
    """User Registration. Check if the username from the form element already
    exists within the Mongo database. If it does, then a message is sent to
    the user. If it does not exist then the new user is inserted in the
    dictionary."""
    # check if a user is already logged in
    if session.get("user"):
        # redirects the user to the get_resources page
        flash("You are already logged in, we will take you to the resources.")
        return redirect(url_for("get_resources"))
    # if the requested method is equal to "POST"
    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            # check if Mongo username matches input for username in form
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then give message
        if existing_user:
            flash("Oh no, this Username already exists...")
            # take the user back to the sign up page
            return redirect(url_for("register"))

        # if no user is found, then insert data in the dictionary
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "bookmarks": []
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # to replace with modal
        flash("Registration successful! You can now view or share resources!")
        # take user to the profile page
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# --- LOG IN FUNCTIONALITY --- #
@app.route("/login", methods=["GET", "POST"])
def login():
    """User Log In. Check if the username from the form element already
    exists within the Mongo database. If it does, then the password is checked
    if it matches the user input. If the password matches then a success
    message is shown. If password does not match then message is shown and user
    is return to log in page. If username does not exist then message is shown
    to user and user is returned to the log in page."""
    # check if a user is already logged in
    if session.get("user"):
        # redirects the user to the get_resources page
        flash("You are already logged in, we will take you to the resources.")
        return redirect(url_for("get_resources"))
    # if the requested method is equal to "POST"
    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then check password
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                # if user password matches hashed password log in user
                session["user"] = request.form.get("username").lower()
                # if user password matches hashed password show message
                flash("Hi {}. Welcome Back!".format(
                    request.form.get("username")))
                # take user to the profile page
                return redirect(url_for("profile", username=session["user"]))
            else:
                # if password does not match show message
                flash("You have entered an invalid username or password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist show message
            flash("You have entered an invalid username or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# --- LOG OUT FUNCTIONALITY --- #
@app.route("/logout")
def logout():
    """User Log Out. Send message to user, remove session and go back to the
    log in page."""
    # show message to user
    flash("You have been logged out")
    # remove user from session cookies
    session.pop("user")
    # return to home page page
    return redirect(url_for("get_featured_resources"))


# --------------------------------------------------- #
# RESOURCE: CREATE | READ | UPDATE | DELETE | SEARCH  #
# --------------------------------------------------- #

# --- CREATE A RESOURCE FUNCTIONALITY --- #
@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    """Add Resource. When user submits a new request, find the resources
    in the database and add the new items to the database. If this was
    successful, the user is notified and returned to the resources page. """
    if not session.get("user"):
        # let user know they needs to register to access this page
        flash("Please register to add a resource")
        return redirect(url_for("register"))
    else:
        if request.method == "POST":
            # find the collections and the keys
            user = mongo.db.users.find_one({'username': session["user"]})
            category = mongo.db.categories.find_one({'category_name':
                                                    request.form.get(
                                                        "category_name")})
            topic = mongo.db.topics.find_one({'topic_name': request.form.get(
                                                        "topic_name")})
            # create dictionary for items in form by ObjectId
            resource = {
                "category_name": ObjectId(category['_id']),
                "resource_name": request.form.get("resource_name"),
                "resource_description": request.form.get(
                    "resource_description"),
                "resource_date": request.form.get("resource_date"),
                "resource_link": request.form.get("resource_link"),
                "topic_name": ObjectId(topic['_id']),
                "created_by": ObjectId(user['_id'])
                }
            mongo.db.resources.insert_one(resource)
            flash("The Resource was successfully added to the Growth Club!")
            return redirect(url_for("get_resources"))
        # find category & topic in database
        categories = mongo.db.categories.find().sort("category_name", 1)
        topics = mongo.db.topics.find().sort("topic_name", 1)
    # render the add_resources template
    return render_template("add_resource.html", categories=categories,
                           topics=topics)


# --- READ RESOURCE FUNCTIONALITY --- #
@app.route("/get_resources")
def get_resources():
    """Get resources function. To find all the resources in the database
    and list them. The ObjectId is used to find the items to ensure it
    can be updated correctly. The ObjectId needs to be translated in a
    way so that it does not show the id number but the name.
    """
    if not session.get("user"):
        # let user know they needs to register to access this page
        flash("Please register to view the Growth Club resources")
        return redirect(url_for("register"))
    else:
        # find resources in the the database
        resources = list(mongo.db.resources.find())
        # loop through all resources
        current_user = mongo.db.users.find_one({'username': session['user']})
        for resource in resources:
            try:
                user = mongo.db.users.find_one({
                    '_id': ObjectId(resource['created_by'])
                })
                category = mongo.db.categories.find_one({
                    '_id': ObjectId(resource['category_name'])
                })
                topic = mongo.db.topics.find_one({
                    '_id': ObjectId(resource['topic_name'])
                })
                if user:
                    resource['created_by'] = user['username']
                else:
                    resource['created_by'] = "Deleted user"
                if category:
                    resource['category_name'] = category['category_name']
                else:
                    resource['category_name'] = "Category deleted"
                if topic:
                    resource['topic_name'] = topic['topic_name']
                else:
                    resource['topic_name'] = "Topic deleted"
                if ObjectId(resource['_id']) in current_user['bookmarks']:
                    resource['bookmarked'] = True
            except Exception:
                pass
    # render the resources template
    return render_template("resources.html", resources=resources)


# --- EDIT A RESOURCE FUNCTIONALITY --- #
@app.route("/edit_resource/<resource_id>", methods=["GET", "POST"])
def edit_resource(resource_id):
    """ Edit Resource. First, retrieve the resource from the database to be
    edited by using the id. Then the ID needs to be converted into a BSON
    data-type. Use the Post method to update the resource in the
    database."""
    if request.method == "POST":
        # find the collections and the keys
        user = mongo.db.users.find_one({'username': session["user"]})
        category = mongo.db.categories.find_one({'category_name':
                                                request.form.get(
                                                    "category_name")})
        topic = mongo.db.topics.find_one({'topic_name': request.form.get(
                                                    "topic_name")})
        submit = {
            "category_name": ObjectId(category['_id']),
            "resource_name": request.form.get("resource_name"),
            "resource_description": request.form.get("resource_description"),
            "resource_date": request.form.get("resource_date"),
            "resource_link": request.form.get("resource_link"),
            "topic_name": ObjectId(topic['_id']),
            "created_by": ObjectId(user['_id'])
        }
        # update resource in database
        mongo.db.resources.update({"_id": ObjectId(resource_id)}, submit)
        flash("The Resource was successfully edited and updated")
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


# --- DELETE A RESOURCE FUNCTIONALITY --- #
@app.route("/delete_resource/<resource_id>")
def delete_resource(resource_id):
    """Delete Resource. Find the resource by id and remove it from the
    database. The present a message to confirm that it has been deleted."""
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("The Resource was successfully deleted")
    # return to the resources page
    return redirect(url_for("get_resources"))


# --- SEARCH FOR A RESOURCE FUNCTIONALITY --- #
@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search Functionality."""
    query = request.form.get("query")
    resources = list(mongo.db.resources.find({"$text": {"$search": query}}))
    for resource in resources:
        try:
            user = mongo.db.users.find_one({
                '_id': ObjectId(resource['created_by'])
            })
            category = mongo.db.categories.find_one({
                '_id': ObjectId(resource['category_name'])
            })
            topic = mongo.db.topics.find_one({
                '_id': ObjectId(resource['topic_name'])
            })
            resource['created_by'] = user['username']
            resource['category_name'] = category['category_name']
            resource['topic_name'] = topic['topic_name']
        except Exception:
            pass
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    topics = list(mongo.db.topics.find().sort("topic_name", 1))
    return render_template("resources.html", resources=resources,
                           categories=categories, topics=topics)


# --------------------------------------------------- #
#   ADMIN MANAGEMENT: FEATURED | CATEGORIES | TOPICS  #
# --------------------------------------------------- #


# --- ADMIN DASHBOARD FUNCTIONALITY --- #
@app.route("/admin_dashboard")
def admin_dashboard():
    """Display Admin Dashboard. ."""
    # check that someone isn't brute-forcing the url get admin functionalities
    if admin():
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        topics = list(mongo.db.topics.find().sort("topic_name", 1))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    # return the admin dashboard template
    return render_template("admin_dashboard.html", categories=categories,
                           topics=topics)


# --- READ FEATURED RESOURCE FUNCTIONALITY --- #
@app.route('/')
@app.route("/get_featured_resources")
def get_featured_resources():
    """Get featured resources function. To find all the resources in the
    database and list them. The ObjectId is used to find the items to ensure it
    can be updated correctly. The ObjectId needs to be translated in a
    way so that it does not show the id number but the name.
    """
    # find featured resources in the the database
    featured_resources = list(mongo.db.featured_resources.find())
    # loop through all resources
    for featured_resource in featured_resources:
        try:
            category = mongo.db.categories.find_one({
                '_id': ObjectId(featured_resource['category_name'])
            })
            topic = mongo.db.topics.find_one({
                '_id': ObjectId(featured_resource['topic_name'])
            })
            # if category exists, display the category
            if category:
                featured_resource['category_name'] = category['category_name']
            # if category does not exists, display the message
            else:
                featured_resource['category_name'] = "No Category"
            # if topic exists, display the topic
            if topic:
                featured_resource['topic_name'] = topic['topic_name']
            # if topic does not exists, display the message
            else:
                featured_resource['topic_name'] = "No Topic"
        except Exception:
            pass
    # render the index template
    return render_template("index.html", featured_resources=featured_resources)


# --- ADD A FEATURED RESOURCE FUNCTIONALITY --- #
@app.route("/add_featured_resource", methods=["GET", "POST"])
def add_featured_resource():
    """Add Featured Resource. When user submits a new request, find the
    resources in the database and add the new items to the database. If this
    was successful, the user is notified and returned to the resources page.
    """
    if admin():
        if request.method == "POST":
            # find the collections and the keys
            category = mongo.db.categories.find_one({'category_name':
                                                    request.form.get(
                                                        "category_name")})
            topic = mongo.db.topics.find_one({'topic_name': request.form.get(
                                                        "topic_name")})
            # create dictionary for items in form by ObjectId
            featured_resource = {
                "category_name": ObjectId(category['_id']),
                "featured_name": request.form.get("featured_name"),
                "featured_description": request.form.get(
                    "featured_description"),
                "featured_date": request.form.get("featured_date"),
                "featured_link": request.form.get("featured_link"),
                "topic_name": ObjectId(topic['_id']),
                "featured_img": request.form.get("featured_img"),
                }
            mongo.db.featured_resources.insert_one(featured_resource)
            flash("Featured Resource Successfully Added")
            return redirect(url_for("get_featured_resources"))
        # find category & topic in database
        categories = mongo.db.categories.find().sort("category_name", 1)
        topics = mongo.db.topics.find().sort("topic_name", 1)
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    # render the add_resources template
    return render_template("add_featured_resource.html", categories=categories,
                           topics=topics)


# --- EDIT A FEATURED RESOURCE FUNCTIONALITY --- #
@app.route("/edit_featured_resource/<featured_resource_id>",
           methods=["GET", "POST"])
def edit_featured_resource(featured_resource_id):
    """ Edit Featured Resource. First, retrieve the resource from the database
    to be edited by using the id. Then the ID needs to be converted into a BSON
    data-type. Use the Post method to update the resource in the
    database."""
    if admin():
        if request.method == "POST":
            # find the collections and the keys
            category = mongo.db.categories.find_one({'category_name':
                                                    request.form.get(
                                                        "category_name")})
            topic = mongo.db.topics.find_one({'topic_name': request.form.get(
                                                        "topic_name")})
            submit = {
                "category_name": ObjectId(category['_id']),
                "featured_name": request.form.get("featured_name"),
                "featured_description": request.form.get(
                    "featured_description"),
                "featured_date": request.form.get("featured_date"),
                "featured_link": request.form.get("featured_link"),
                "topic_name": ObjectId(topic['_id']),
            }
            # update resource in database
            mongo.db.featured_resources.update({
                                "_id": ObjectId(featured_resource_id)}, submit)
            flash("The Featured Resource was successfully edited and updated")
            # return to the resources page
            return redirect(url_for("get_featured_resources"))
        # retrieve the featured resource from the database by id
        featured_resource = mongo.db.featured_resources.find_one({
            "_id": ObjectId(featured_resource_id)})
        # find the category & topic from the database
        categories = mongo.db.categories.find().sort("category_name", 1)
        topics = mongo.db.topics.find().sort("topic_name", 1)
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    # render the edit_resources template
    return render_template("edit_featured_resource.html",
                           featured_resource=featured_resource,
                           categories=categories, topics=topics)


# --- DELETE A FEATURED RESOURCE FUNCTIONALITY --- #
@app.route("/delete_featured_resource/<featured_resource_id>")
def delete_featured_resource(featured_resource_id):
    """Delete Featured Resource. Find the resource by id and remove it from the
    database. The present a message to confirm that it has been deleted."""
    mongo.db.featured_resources.remove({"_id": ObjectId(featured_resource_id)})
    flash("The Featured Resource was successfully deleted")
    # return to the resources page
    return redirect(url_for("get_featured_resources"))


# --- ADD A CATEGORY FUNCTIONALITY --- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ Add Category. If the function is called using the POST method, then
    the data from the form is retrieved, and inserted into the database.
    Otherwise it will display the empty form."""
    if admin():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            # insert the category in the database
            mongo.db.categories.insert_one(category)
            flash("The new Category was added")
            # return to the admin dashboard page
            return redirect(url_for("admin_dashboard"))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    # return to the add_category page
    return render_template("add_category.html")


# --- EDIT A CATEGORY FUNCTIONALITY --- #
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ Edit Category Functionality. If the user submits an edit request, then
    the Category is retrieved from the database, updated in the database and
    after the user receives a message, they are taken back to the manage page.
    """
    if admin():
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            # update the category in the database
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Updated")
            # user returned to the admin dashboard page
            return redirect(url_for("admin_dashboard"))
        # Using the category ID being sent into this function, the .find_one()
        # method is used on the categories collection
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    return render_template("edit_category.html", category=category)


# --- DELETE A CATEGORY FUNCTIONALITY --- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """ Delete Category Functionality. If the user wants to delete a category,
    then using the remove() method, it is deleted in the database. Thereafter,
    the user receives a message and they are taken back to the manage page. """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("admin_dashboard"))


# --- ADD A TOPIC FUNCTIONALITY --- #
@app.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    """ Add Topic. If the function is called using the POST method, then
    the data from the form is retrieved, and inserted into the database.
    Otherwise it will display the empty form."""
    if admin():
        if request.method == "POST":
            topic = {
                "topic_name": request.form.get("topic_name")
            }
            # insert the category in the database
            mongo.db.topics.insert_one(topic)
            flash("The new Topic was Added")
            # return to the manage admin dashboard page
            return redirect(url_for("admin_dashboard"))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    # return to the add_category page
    return render_template("add_topic.html")


# --- EDIT A TOPIC FUNCTIONALITY --- #
@app.route("/edit_topic/<topic_id>", methods=["GET", "POST"])
def edit_topic(topic_id):
    """ Edit Topic Functionality. If the user submits an edit request, then
    the Category is retrieved from the database, updated in the database and
    after the user receives a message, they are taken back to the manage page.
    """
    if admin():
        if request.method == "POST":
            submit = {
                "topic_name": request.form.get("topic_name")
            }
            # update the topic in the database
            mongo.db.topics.update({"_id": ObjectId(topic_id)}, submit)
            flash("Topic Successfully Updated")
            # user returned to the admin dashboard page
            return redirect(url_for("admin_dashboard"))
        # Using the topic ID being sent into this function, the .find_one()
        # method is used on the topics collection
        topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_resources"))
    return render_template("edit_topic.html", topic=topic)


# --- DELETE A TOPIC FUNCTIONALITY --- #
@app.route("/delete_topic/<topic_id>")
def delete_topic(topic_id):
    """ Delete Topic Functionality. If the user wants to delete a topic,
    then using the remove() method, it is deleted in the database. Thereafter,
    the user receives a message and they are taken back to the admin dahboard
    page. """
    mongo.db.topics.remove({"_id": ObjectId(topic_id)})
    flash("Topic Successfully Deleted")
    return redirect(url_for("admin_dashboard"))


# --------------------------------------------------- #
#           USER FEATURES: PROFILE | BOOKMARK         #
# --------------------------------------------------- #

# --- PROFILE  FUNCTIONALITY --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """User Profile. Find username in the database and retrieve the
    username. Then render the profile template with the user's name"""
    if 'user' in session:
        # find the user in the database
        user = mongo.db.users.find_one(
            # take the session user's username from Mongo
            {"username": session["user"]})
        # if the user has a bookmark try the execute the below
        try:
            # check if session['user'] cookie is truthy
            if session["user"]:
                user_resources = []
                for resource in user['bookmarks']:
                    user_resource = mongo.db.resources.find_one({
                        '_id': resource})
                    if user_resource:
                        user = mongo.db.users.find_one({
                            '_id': ObjectId(user_resource['created_by'])
                        })
                        category = mongo.db.categories.find_one({
                            '_id': ObjectId(user_resource['category_name'])
                        })
                        topic = mongo.db.topics.find_one({
                            '_id': ObjectId(user_resource['topic_name'])
                        })
                        if user:
                            user_resource['created_by'] = user[
                                'username']
                        else:
                            user_resource['created_by'] = "No User"
                        if category:
                            user_resource['category_name'] = category[
                                'category_name']
                        else:
                            user_resource['category_name'] = "No Category"
                        if topic:
                            user_resource['topic_name'] = topic['topic_name']
                        else:
                            user_resource['topic_name'] = "No Topic"
                    else:
                        user_resource = dict()
                        user_resource['_id'] = resource
                        user_resource['created_by'] = "N/A"
                        user_resource['category_name'] = "N/A"
                        user_resource['topic_name'] = "Resource deleted"
                    user_resources.append(user_resource)
                # render appropriate profile template
                return render_template(
                    "profile.html", username=username,
                    resources=user_resources)
        # if the user has no bookmarks try render their profile
        except KeyError:
            pass
    # return profile page with user's unique name
    return render_template("profile.html", username=username)


# --- BOOKMARK A RESOURCE FUNCTIONALITY --- #
@app.route("/bookmark/<resource_id>", methods=["POST"])
def bookmark(resource_id):
    """ Bookmark Functionality."""
    if request.method == "POST":
        user_bookmarks = list(mongo.db.users.find_one({"username": session
                                                      ["user"].lower()})
                              ['bookmarks'])
        if ObjectId(resource_id) not in user_bookmarks:
            mongo.db.users.find_one_and_update(
                {"username": session["user"].lower()},
                {"$push": {"bookmarks": ObjectId(resource_id)}})
            flash("Resource added your bookmarks on your profile")
        else:
            flash("Resource already bookmarked, skipping")
        return redirect(url_for(
                        "profile", username=session["user"]))

    return redirect(url_for(
                        "profile", username=session["user"]))


# --- DELETE A BOOKMARK FUNCTIONALITY --- #
@app.route("/delete_bookmark/<resource_id>")
def delete_bookmark(resource_id):
    """ Delete Bookmark Functionality."""
    try:
        mongo.db.users.find_one_and_update(
            {"username": session["user"].lower()},
            {"$pull": {"bookmarks": ObjectId(resource_id)}})
        flash("Bookmark Successfully Removed")
    except Exception:
        user_bookmarks = mongo.db.users.find_one({"username": session["user"].
                                                 lower()})['bookmarks']
        user_bookmarks.remove(resource_id)
        mongo.db.users.find_one_and_update({"username": session["user"].
                                            lower()}, {'$set': {"bookmarks":
                                                                user_bookmarks
                                                                }})
    finally:
        return redirect(url_for(
                        "profile", username=session["user"]))


# --- CHANGE PASSWORD FUNCTIONALITY --- #
@app.route('/change_password/<username>', methods=["GET", "POST"])
def change_password(username):
    """
    Change Password Functionality where the user can change their current
    password on their profile page.
    """
    if request.method == "POST":
        newPassword = generate_password_hash(request.form.get
                                             ("password_change"))
        mongo.db.users.update(
            {"username": username},
            {'$set':
                {"password": newPassword}})
        flash("Your password has been updated")
        return redirect(url_for("get_resources"))
    if session:
        return redirect(url_for("get_resources"))
    return redirect(url_for(
                        "profile", username=session["user"]))


# --- DELETE PROFILE FUNCTIONALITY --- #
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    """
    Delete Profile Functionality where the user can delete their account
    on their profile page.
    """
    user = mongo.db.users.find_one({'username': session["user"]})
    # Checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm_to_delete")):
        flash("We can confirm that your account has been deleted.")
        session.pop("user")
        mongo.db.users.remove({"_id": ObjectId(user['_id'])})
        return redirect(url_for("get_featured_resources"))
    else:
        flash("The password you entered was incorrect. Please try again!")
        return redirect(url_for("profile", user=user.get("username")))
    # return to home page page
    return redirect(url_for("get_featured_resources"))


# --------------------------------------------------- #
#                    ERROR HANDELING                  #
# --------------------------------------------------- #

# -- 401 ERROR --- #
@app.errorhandler(401)
def unauthorized_access(e):
    """
    Renders a custom 401 error page with a button
    that takes the user back to the log in or register pages.
    """
    return render_template('errors/401.html'), 401


# -- 404 ERROR --- #
@app.errorhandler(404)
def page_not_found(e):
    """
    Renders a custom 404 error page with a button
    that takes the user back to the home page.
    """
    return render_template('errors/404.html'), 404


# -- 500 ERROR --- #
@app.errorhandler(500)
def not_found_server(e):
    """
    Renders a custom 500 error page with a button
    that takes the user back to the home page.
    """
    return render_template('errors/500.html'), 500


# --------------------------------------------------- #
#                       MISC                          #
# --------------------------------------------------- #


# --- RENDER LANDING PAGE FUNCTIONALITY --- #
@app.route('/')
@app.route('/index')
def index():
    """Render Landing page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
