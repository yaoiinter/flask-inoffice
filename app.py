# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = 'hahaha'

manager = Manager(app)
# 使用bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/list/<fruit>')
def listTest(fruit):
    testList = ["apple", "orange", "pineapple"]
    return render_template('user.html', fruit=testList)

@app.route('/login', methods=['GET', 'POST'])
def login():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    manager.run()
