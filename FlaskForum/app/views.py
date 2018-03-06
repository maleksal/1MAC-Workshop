from flask import render_template, request, redirect, url_for
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html",posts = post_store.get_all())

@app.route("/add_post",methods= ["GET","POST"])
def add_post():
    if request.method == "POST":
        new_post = models.Post(request.form["Title"], request.form["Content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("add_post.html")
@app.route("/members")
def members():
    return render_template("members.html",members=member_store.get_all())
@app.route("/post")
def get_post():
    return render_template("posts.html",post= post_store.get_all())
@app.route("/contact")
def contact_us():
    return render_template("contact.html")


