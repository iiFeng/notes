from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField
from wtforms.validators import DataRequired, Length


class noteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    message = StringField('Message', validators=[DataRequired(), Length, 200])
    submit = SubmitField('submit')
