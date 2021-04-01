from app import app, db
from flask import render_template, redirect, url_for

from app.models.forms import PostForm
from app.models.tables import Post


def handle_register(post_id):
    new_post = Post.query.filter_by(id=post_id).first()
    new_post.registered = not new_post.registered
    db.session.commit()


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, handle_register=handle_register)


@app.route("/new", methods=["GET", "POST"])
def new():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(form.title.data, form.description.data, form.where.data, form.date.data, form.image.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("new.html", form=form)
