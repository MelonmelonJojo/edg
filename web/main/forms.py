from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SelectField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_pagedown.fields import PageDownField


class LoginForm(FlaskForm):
    email = StringField('Username or Email',
                        validators=[DataRequired(), Length(1, 64), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20,
                                                            'Length out off range, should not longer than 20 characters'),
                                                     Regexp('^[A-Za-z0-9]+$', 0,
                                                            message='Your password contain invalid characters.')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20,
                                                            'Length out off range, should not longer than 20 characters'),
                                                     Regexp('^[A-Za-z0-9]+$', 0,
                                                            message='Your password contain invalid characters.')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords not match. Please try again')])
    sex = RadioField('Sex', choices=[(1, 'Male'), (0, 'Female')],
                     validators=[DataRequired()])
    tel = StringField('Mobile Number', validators=[DataRequired(), Length(10, 11),
                                                   Regexp('^[0-9]+$', message='Please enter a valid mobile number')])
    submit = SubmitField('Submit')


class ProgrammeForm(FlaskForm):
    name = StringField('Programme Name', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()])
    age_range = SelectField('Age Range', choices=[(0, '12-14'), (1, '15-18'), (2, 'Adult')],
                            validators=[DataRequired()])
    thumbnail = FileField('Thumbnail',
                          validators=[DataRequired(),
                                      Regexp('^[^/\\]\.(jpg)(png)$', message='Please upload .jpg or .png file')])
    bg_image = FileField('Background Image',
                         validators=[DataRequired(),
                                     Regexp('^[^/\\]\.(jpg)(png)$', message='Please upload .jpg or .png file')])
    body = PageDownField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    role_name = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    category_name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
