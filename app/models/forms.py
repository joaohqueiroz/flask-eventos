from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    where = StringField("where", validators=[DataRequired()])
    date = DateTimeField("date", format='%d/%m/%Y %H:%M', validators=[DataRequired()])
    image = StringField("image")
