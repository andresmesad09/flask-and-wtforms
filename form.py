from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email(), Length(min=8)])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")
