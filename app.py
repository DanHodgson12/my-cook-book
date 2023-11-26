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

mongo = PyMongo(app)


@app.route("/")
@app.route("/recipes/")
def recipes():
    recipes = list(mongo.db.recipes.find())
    meal_types = mongo.db.meal_types.find()
    return render_template(
        "recipes.html", recipes=recipes, meal_types=meal_types)


@app.route("/recipes/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    meal_types = mongo.db.meal_types.find()
    return render_template(
        "view_recipe.html", recipe=recipe, meal_types=meal_types)


@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    if request.method == "POST":
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$addToSet": {"my_cookbook": recipe_id}}
        )
        flash("Recipe Successfully Saved", "success")

    return redirect(url_for("view_recipe", recipe_id=recipe_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "my_cookbook": []
        }

        mongo.db.users.insert_one(new_user)

        # put the new_user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful", "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")), "success")
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("sign_in"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        recipes = list(mongo.db.recipes.find())
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    flash("You have been logged out", "success")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        all_ingredients = []
        ingredients = request.form.get("ingredients").split('\n')
        for i in ingredients:
            if i.strip():
                all_ingredients.append(i)

        whole_method = []
        for i in request.form.getlist("step_desc[]"):
            if i == "":
                continue
            else:
                whole_method.append(i)

        recipe_img = {}
        if request.form.get("recipe_img") == "":
            recipe_img = {
                "src": "",
                "alt": ""
            }
        else:
            recipe_img = {
                "src": request.form.get("recipe_img"),
                "alt": "Image of {0} recipe.".format(
                    request.form.get("recipe_name"))
            }

        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_desc": request.form.get("recipe_desc"),
            "meal_type": request.form.get("meal_type"),
            "serves": request.form.get("serves"),
            "ready_in": {
                "hours": request.form.get("ready_hours"),
                "minutes": request.form.get("ready_minutes")
            },
            "ingredients": all_ingredients,
            "method": whole_method,
            "created_by": session["user"],
            "recipe_img": recipe_img
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Recipe Successfully Added", "success")
        return redirect(url_for("recipes"))

    meal_types = mongo.db.meal_types.find()
    return render_template("add_recipe.html", meal_types=meal_types)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        all_ingredients = []
        ingredients = request.form.get("ingredients").split('\n')
        for i in ingredients:
            if i.strip():
                all_ingredients.append(i)

        whole_method = []
        for i in request.form.getlist("step_desc[]"):
            if i == "":
                continue
            else:
                whole_method.append(i)

        recipe_img = {}
        if request.form.get("recipe_img") == "":
            recipe_img = {
                "src": "",
                "alt": ""
            }
        else:
            recipe_img = {
                "src": request.form.get("recipe_img"),
                "alt": "Image of {0} recipe.".format(
                    request.form.get("recipe_name"))
            }

        edited_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_desc": request.form.get("recipe_desc"),
            "meal_type": request.form.get("meal_type"),
            "serves": request.form.get("serves"),
            "ready_in": {
                "hours": request.form.get("ready_hours"),
                "minutes": request.form.get("ready_minutes")
            },
            "ingredients": all_ingredients,
            "method": whole_method,
            "created_by": session["user"],
            "recipe_img": recipe_img
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {'$set': edited_recipe})
        flash("Recipe Successfully Updated", "success")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    meal_types = mongo.db.meal_types.find()
    return render_template(
        "edit_recipe.html", recipe=recipe, meal_types=meal_types)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted", "success")
    return redirect(url_for("recipes"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
