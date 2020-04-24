from flask import render_template, flash, redirect, url_for
from auth import app, db, bcrypt
from auth.forms import LoginForm, RegistrationForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('auth/home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)

@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data} !', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)