from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
class RegisterForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address:',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6)])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='submit')

    def set_password(self, password):
        self.password1 = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password1, password)

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6)])
    submit = SubmitField(label='Login')

