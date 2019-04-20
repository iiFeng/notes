from flask import flash, render_template, url_for, redirect

from sayhello import app, db
from sayhello.forms import noteForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = noteForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('your message have been sent to the world')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
