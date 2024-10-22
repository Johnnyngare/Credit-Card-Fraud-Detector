from flask import Flask, redirect, url_for, session, request, flash, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SESSION_COOKIE_SECURE'] = False  # For local development
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Google OAuth setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='651076523016-kba17q4ljlo6apmbijdosu0girrpk5sk.apps.googleusercontent.com',  # Replace with your Google Client ID
    client_secret='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',  # Replace with your Google Client Secret
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

# Simulate a user database
users = {}

class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/login')
def login():
    session.permanent = True  # Enable session lifetime
    if current_user.is_authenticated:  # If user is already logged in
        return redirect(url_for('index'))  # Redirect to the index page
    return google.authorize_redirect(
        redirect_uri=url_for('authorize', _external=True)
    )

@app.route('/authorize')
def authorize():
    try:
        token = google.authorize_access_token()
        resp = google.get('userinfo')  # Get user info
        user_info = resp.json()

        user_id = user_info['sub']
        user_name = user_info.get('name', '')
        user_email = user_info.get('email', '')

        # Check if the user already exists in our "database"
        if user_id not in users:
            users[user_id] = User(user_id, user_name, user_email)

        # Log in the user
        user = users[user_id]
        login_user(user)

        # Clear OAuth session data
        session.pop('_google_authlib_state_', None)
        session.pop('_google_authlib_nonce_', None)

        # Redirect to the index.html page after login
        return redirect(url_for('index'))

    except Exception as e:
        print(f"Authorization error: {str(e)}")
        flash('Authentication failed. Please try again.', 'error')
        return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()  # Clear session data
    flash('You have logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def home():
    if current_user.is_authenticated:  # If the user is already logged in, redirect to index
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))  # Otherwise, go to the login page

if __name__ == '__main__':
    app.run(debug=True, port=5000)
