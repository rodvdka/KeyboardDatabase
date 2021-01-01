from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class InsertKeyboardForm(FlaskForm):
    brand = StringField("Brand", validators=[DataRequired(), Length(min=2, max=64)])
    name = StringField("Keyboard Model", validators=[DataRequired(), Length(min=2, max=64)])
    model = StringField("Model ID", validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField("Submit")

class InsertKeysetForm(FlaskForm):
    brand = StringField("Brand", validators=[DataRequired(), Length(min=2, max=64)])
    name = StringField("Keyset Name", validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    search = StringField("Search", validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField("Submit")