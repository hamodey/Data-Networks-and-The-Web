from flask import Flask, render_template, request, jsonify, flash
from flask_bootstrap import Bootstrap
from flask import redirect, url_for
from vs_url_for import vs_url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, validators
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = "s3cretK3y"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@localhost/my_app'
login_manager = LoginManager()

Bootstrap(app)
db = SQLAlchemy(app)
login_manager.init_app(app)

class addOrderForm(FlaskForm):
    text = StringField('text', validators = [InputRequired(), Length(min=1, max=255)])
    #userID = StringField('text', validators = [InputRequired(), Length(min=1, max=255)])


class editOrderForm(FlaskForm):
    #orderID = StringField('text', validators = [InputRequired(), Length(min=1, max=255)])
    #userID = StringField('text', validators = [InputRequired(), Length(min=1, max=255)])
    text = StringField('text', validators = [InputRequired(), Length(min=1, max=255)])

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    FirstName = StringField('FirstName', validators=[InputRequired(), Length(min=4, max=15)])
    LastName = StringField('LastName', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))

    def get_id(self):
        return self.id
    def get_name(self):
        return self.FirstName + self.LastName    

class orders(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    userID = db.Column(db.Integer)
    username = db.Column(db.String(255))

    def __repr__(self):
        return self.Description

@login_manager.user_loader
def load_user(id):
    return users.query.get(int(id))

@app.route('/user', methods=['GET'])
def get_all_orders():
    
    return ''

@app.route('/user/<id>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/add_order', methods=['GET', 'POST'])
@login_required
def add_order():
    form = addOrderForm()
    if form.validate_on_submit():
        full_name = current_user.FirstName + current_user.LastName
       # hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_order = orders(text = form.text.data, userID = current_user.id, username = full_name)
        db.session.add(new_order)
        db.session.commit()
        return redirect(vs_url_for('show_orders'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('add_order.html', form=form)
    # return '<h1>Fail</h1>'


@app.route('/edit_order/<id>', methods=['GET', 'POST'])
@login_required
def edit_order(id):
    form = editOrderForm()
    updated = orders.query.filter_by(orderID=id).first()
    #if not updated:
        #return '<h1> no order found </h1>'
    #return redirect(vs_url_for('show_orders'))
    form = editOrderForm();
    form.orderID = updated.orderID
    updated.text = form.text.data
    db.session.commit()
    if form.validate_on_submit():
        return redirect(vs_url_for('show_orders'))
    return render_template('edit_order.html', form=form)

@app.route('/delete_user/<id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    user = users.query.filter_by(id=id).first()
    if not user:
        return "<h1>no user found</h1>"

    db.session.delete(user)
    db.session.commit()
    return '<h1> user deleted</h1>'

@app.route('/delete_order/<id>', methods=['GET', 'POST'])
@login_required
def delete_order(id):
    order = orders.query.filter_by(orderID=id).first()
    if not order:
        return "<h1>no order found</h1>"

    db.session.delete(order)
    db.session.commit()
    return '<h1> order deleted</h1>'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(vs_url_for('dashboard'))
        return '<h1>Incorrect password or username</h1>'        
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = users(FirstName = form.FirstName.data, LastName=form.LastName.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user added</h1>'
	# return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    form = users.query.all()
    return render_template('orders.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(vs_url_for('index'))


@app.route('/orders')
@login_required
def show_orders():
    form = orders.query.all()
    return render_template('total.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
