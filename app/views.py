from flask import render_template, flash, redirect
from app import app
from .forms import CviForm


@app.route('/')
@app.route('/index')
def index():
    cvi = {'project': 'Gordon Rooms'}
    line_items = [  # fake array of posts
        {
            'line_number': '10',
            'item': 'A task to do some work!'
        },
        {
            'line_number': '11',
            'item': 'Another line item!'
        }
    ]
    return render_template(
        'index.html',
        title="Home",
        cvi=cvi,
        line_items=line_items
    )


@app.route('/cvi', methods=['POST', 'GET'])
def cvi():
    form = CviForm()
    if form.validate_on_submit():
        # flash('Login requested for OpenID="%s", remember_me=%s' %
        #       (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template(
        'login.html',
        title="cvi",
        form=form,

    )
