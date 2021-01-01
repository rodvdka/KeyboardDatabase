from keebs import app, SearchForm, db
from keebs.forms import InsertKeyboardForm, InsertKeysetForm
from keebs.models import Keyboard, Keyset
from flask import render_template, flash

@app.route("/")
def home():
    return render_template("home.jinja")

@app.route("/keyboards")
def keyboards():
    return render_template("keyboards.jinja", keyboards=Keyboard.query.all())

@app.route("/keysets")
def keysets():
    return render_template("keysets.jinja", keysets=Keyset.query.all())

@app.route("/about")
def about():
    return render_template("about.jinja")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    keyboard_form = InsertKeyboardForm()
    keyset_form = InsertKeysetForm()
    if keyboard_form.validate_on_submit():
        db.session.add(Keyboard(brand=keyboard_form.brand.data, name=keyboard_form.name.data, model=keyboard_form.model.data))
        db.session.commit()
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