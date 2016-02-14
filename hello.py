# -*- coding: utf-8 -*-
# 2016-2-11
# IOT 微妙物联平台 基于IOT的物联网平台架构
# 邯郸金世达科技  高胜

"""
启动
"""
from flask.ext.bootstrap import Bootstrap
from flask import Flask,render_template
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ailaohuu_12'
bootstrap = Bootstrap(app)


"""
SQLAlchemy
"""
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

"""
Model
"""
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username



"""
form 表单
"""

class NameForm(Form):
    name = StringField(u'姓 名:', validators=[Required()])
    mpwd = PasswordField(u'密 码:')
    submit = SubmitField(u'确定')


"""
路由
"""
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/')
def index():
    name = None
    mpwd = None
    form = NameForm()
    if form.validate_on_submit():
       name = form.name.data
       mpwd = form.mpwd.data
       form.name.data = ''
    return render_template('index.html', form=form, name=name)
#    return  render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello,%s</h1>' % name
    return  render_template('user.html',name=name)


"""
入口
"""
if __name__ == '__main__':
    app.run(debug=True)
