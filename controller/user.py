from flask import render_template
from controller import app
# from forms.user import LoginForm


# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)