from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, ValidationError, Length, EqualTo


# checks if a field contains characters that are not allowed
def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):
    username = StringField(validators=[Required()])
    firstname = StringField(validators=[Required(), character_check])
    lastname = StringField(validators=[Required(), character_check])
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
