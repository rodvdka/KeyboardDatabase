import os

from PIL import Image
from keebs import app, SearchForm, db
from keebs.forms import InsertKeyboardForm, InsertKeysetForm
from keebs.models import Keyboard, Keyset
from flask import render_template, flash

@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/keyboards")
def keyboards():
    return render_template("keyboards.jinja", keyboards=Keyboard.query.all())

@app.route("/keyboard/<int:keyboard_id>")
def keyboard(keyboard_id):
    return render_template("keyboard.jinja", keyboard=Keyboard.query.get_or_404(keyboard_id))

@app.route("/keysets")
def keysets():
    return render_template("keysets.jinja", keysets=Keyset.query.all())

@app.route("/keyset/<int:keyset_id>")
def keyset(keyset_id):
    return render_template("keyset.jinja", keyset=Keyset.query.get_or_404(keyset_id))

@app.route("/about")
def about():
    return render_template("about.jinja")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    keyboard_form = InsertKeyboardForm()
    keyset_form = InsertKeysetForm()
    if keyboard_form.validate_on_submit():
        kb = Keyboard(brand=keyboard_form.brand.data, name=keyboard_form.name.data, model=keyboard_form.model.data)
        db.session.add(kb)
        db.session.commit()
        save_image(kb.id, keyboard_form.image.data)
        flash(f"Submitted {keyboard_form.name.data}!")
    elif keyset_form.validate_on_submit():
        db.session.add(Keyset(brand=keyset_form.brand.data, name=keyset_form.name.data))
        db.session.commit()
        flash(f"Submitted {keyset_form.name.data}!")
    return render_template("insert.jinja", keyboard_form=keyboard_form, keyset_form=keyset_form)

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f"Searching for {form.search.data}!")
        #return redirect(url_for("home"))
    print(form.__dict__)
    return render_template("search.jinja", title="search", form=form)

def save_image(id, data):
    img = Image.open(data)
    #img.thumbnail(125, 125)
    path = os.path.join(app.root_path, "static/images/keyboard/", str(id) + os.path.splitext(data.filename)[1])
    img.save(path)