import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, ValidationError, Length, EqualTo, InputRequired


class RegisterForm(FlaskForm):
    firstname = StringField(validators=[InputRequired()])
    lastname = StringField(validators=[InputRequired()])
    email = StringField(validators=[InputRequired(), Email()])
    phone = StringField(validators=[InputRequired()])
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(
                min=6,
                max=12,
                message="Password must be between 6 and 12 characters in length."
            )
        ]
    )
    password_confirm = PasswordField(
        validators=[
            InputRequired(),
            EqualTo("password", message="Both password fields must be equal!")
        ]
    )
    submit = SubmitField()

    def validate_password(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)')
        if not p.match(self.password.data):
            raise ValidationError(message="Password must contain at least 1 small letter,"
                                          " 1 capital letter, 1 digit and 1 special character.")


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField()
