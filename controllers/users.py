from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.users import User

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.get_user_by_email(email=email)
        
        if user:
            if password == user[-1]:
                return redirect(url_for('pagamentos'))
            
        flash('Email ou senha incorretos.', category='error')
        return render_template('login.html')
    
    return render_template('login.html')

@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form.to_dict()
                
        user = User(data)
                
        if not user.is_unique():
            flash('Email já cadastrado', category='error')
            return render_template('signup.html')
        else:
            user.save()
            return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')
