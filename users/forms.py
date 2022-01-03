from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, ValidationError, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(validators=[Required()])
    firstname = StringField(validators=[Required()])
    lastname = StringField(validators=[Required()])
    email = StringField(validators=[Required(), Email()])
    phone = StringField(validators=[Required()])
    password = PasswordField(
        validators=[
            Required(),
            Length(
                min=6,
                max=12,
                message="Password must be between 6 and 12 characters in length.",
            ),
        ]
    )
    password_confirm = PasswordField(
        validators=[
            Required(),
            EqualTo("password", message="Both password fields must be equal!"),
        ]
    )
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()
