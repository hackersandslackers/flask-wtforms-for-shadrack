from flask import url_for, render_template, redirect
from flask import current_app as app
from .forms import InfoForm


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')


@app.route('/apply', methods=('GET', 'POST'))
def new_apply():
    form = InfoForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('apply.html',
                           form=form,
                           template='form-template')


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')
