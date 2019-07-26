from flask import session, redirect, url_for, flash
from functools import wraps
# from wtforms import Form, StringField, TextAreaField , PasswordField, validators

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized , Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

