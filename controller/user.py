# -*- coding: utf-8 -*-

from flask import redirect, request, render_template, flash
from controller import app
from environ import name,mypassword,check_hash,get_hash

# from forms.user import LoginForm


# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/admin')
def load_admin():
    return render_template('admin.html')


@app.route('/admin', methods=['GET','POST'])
def admin():
    username = request.form['username']
    password = request.form['password']
    if username==name and password==mypassword:
        return '''
        <h1>Logged in</h1>
        '''
    else:
        flash(u'نام کاربری یا رمز عبور خود را اشتباه وارد کردید')
        return redirect('/admin')




def log_out():
    pass