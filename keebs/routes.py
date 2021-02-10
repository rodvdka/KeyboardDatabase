import base64
import os

from PIL import Image
from keebs import app, SearchForm, db, helper
from keebs.forms import InsertKeyboardForm
from keebs.models import Keyboard
from flask import render_template, flash, request

def render(template, **kwargs):
    search_form = SearchForm()
    if search_form.validate_on_submit():
        pass
    return render_template(template, search_form=search_form, **kwargs)

@app.route("/")
def index():
    return render("index.jinja")

@app.route("/inventory")
def inventory():
    return render("inventory.jinja", items=Keyboard.query.all())

@app.route("/item/<int:item_id>")
def item(item_id):
    return render("item.jinja", item=Keyboard.query.get_or_404(item_id))

@app.route("/gallery")
def gallery():
    return render("gallery.jinja")

@app.route("/about")
def about():
    return render("about.jinja")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    form = InsertKeyboardForm()
    if form.validate_on_submit():
        img64 = helper.to_img64(request.files["image"])
        kb = Keyboard(brand=form.brand.data, name=form.name.data, model=form.model.data, switch=form.switch.data, desc=form.desc.data, quantity=form.quantity.data, price=form.price.data, image=img64)
        db.session.add(kb)
        db.session.commit()
        flash(f"Submitted {form.name.data}!")
    return render("insert.jinja", keyboard_form=form)

@app.route("/search")
def search():
    query = request.args("search")
    form = SearchForm()
    # if form.validate_on_submit():
    #     flash(f"Searching for {form.search.data}!")
    #     #return redirect(url_for("home"))
    # print(form.__dict__)
    return render("search.jinja", title="search", form=form, query=query)

if os.environ["INITDB"] == "1":
    print("TEST")
    db.create_all()
    db.session.add(Keyboard(brand="IBM", name="5251 Beamspring", model="5251", switch="Beamspring", desc="Terminal item", quantity=1, price=1))
    db.session.commit()