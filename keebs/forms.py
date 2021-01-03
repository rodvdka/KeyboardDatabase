from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InsertKeyboardForm(FlaskForm):
    kw = {"title": "Keyboard Form", "id": "keyboard-form"}
    brand = StringField("Brand", validators=[DataRequired(), Length(min=2, max=64)])
    name = StringField("Keyboard Model", validators=[DataRequired(), Length(min=2, max=64)])
    model = StringField("Model ID", validators=[DataRequired(), Length(min=2, max=64)])
    switch = StringField("Switch", validators=[DataRequired(), Length(min=2, max=64)])
    image = FileField("Image", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Submit")

class InsertKeysetForm(FlaskForm):
    kw = {"title": "Keyset Form", "id": "keyset-form"}
    brand = StringField("Brand", validators=[DataRequired(), Length(min=2, max=64)])
    name = StringField("Keyset Name", validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    kw = {"title": "Search Form", "id": "search-form"}
    search = StringField("Search", validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField("Submit")