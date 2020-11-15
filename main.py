from flask import Flask, render_template, request, url_for, redirect
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm, Form
from wtforms.widgets import html_params, HTMLString


app = Flask(__name__, instance_relative_config=False)
app.secret_key = 'SH'


class ContactForm(FlaskForm):
    """Contact form."""
    name = TextField('Nam', [
        DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success.html'))
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)