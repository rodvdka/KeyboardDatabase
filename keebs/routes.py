from keebs import app, SearchForm, db, helper
from keebs.forms import KeyboardForm, AddCartForm
from keebs.helper import to_img64, add_to_cart, check_session, purge_cart
from keebs.models import Keyboard
from flask import render_template, flash, request, session


def render(template, **kwargs):
    search_form = SearchForm()
    if search_form.validate_on_submit():
        pass
    return render_template(template, search_form=search_form, **kwargs)

@app.route("/")
def index():
    return render("index.jinja")

@app.route("/about")
def about():
    purge_cart()
    return render("about.jinja")

@app.route("/gallery")
def gallery():
    return render("gallery.jinja", items=Keyboard.query.all())

@app.route("/inventory")
def inventory():
    return render("inventory.jinja", items=Keyboard.query.all())

@app.route("/item/<int:item_id>", methods=["GET", "POST"])
def item(item_id):
    cart_form = AddCartForm()
    item = Keyboard.query.get_or_404(item_id)

    # If we are posting to this route and the cart form is valid, push item into the session cart
    if request.method == "POST" and cart_form.validate_on_submit():
        add_to_cart(item)
    return render("item.jinja", item=item, cart_form=cart_form)

@app.route("/insert", methods=["GET", "POST"])
def insert():
    form = KeyboardForm()
    if form.validate_on_submit():
        img64_small = to_img64(request.files["image"], 200)
        img64_large = to_img64(request.files["image"], 600)
        kb = Keyboard(brand=form.brand.data, name=form.name.data, model=form.model.data, switch=form.switch.data, desc=form.desc.data, quantity=form.quantity.data, price=form.price.data, img_small=img64_small, img_large=img64_large)
        db.session.add(kb)
        db.session.commit()
        flash(f"Submitted {form.name.data}!")
    return render("insert.jinja", form=form)

@app.route("/cart")
def cart():
    entries = {}
    for x in session["cart"].keys():
        entries[x] = {"item": Keyboard.query.get_or_404(x), "quantity": session["cart"][x]["quantity"]}
    return render("cart.jinja", entries=entries.values())

@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update(item_id):
    item = Keyboard.query.get_or_404(item_id)
    form = KeyboardForm()
    if request.method == "GET":
        form.process(obj=item)
    elif request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(item)
            if form.image.data:
                item.img_small = helper.to_img64(request.files["image"], 200)
                item.img_large = helper.to_img64(request.files["image"], 600)
            db.session.add(item)
            db.session.commit()
            print("return inv")
            return inventory()
    return render("update.jinja", title="Update", item=item, form=form)

@app.route("/search")
def search():
    query = request.args("search")
    form = SearchForm()
    # if form.validate_on_submit():
    #     flash(f"Searching for {form.search.data}!")
    #     #return redirect(url_for("home"))
    # print(form.__dict__)
    return render("search.jinja", title="search", form=form, query=query)