import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  # In production, use a proper secret key

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database setup
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.executescript(f.read())
    db.commit()

@app.cli.command('init-db')
def init_db_command():
    init_db()
    print("Database initialized.")

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_logged_in():
    return 'user_id' in session

def get_current_user():
    if is_logged_in():
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
        return user
    return None

# Routes
@app.route('/')
def index():
    if is_logged_in():
        db = get_db()
        posts = db.execute(
            'SELECT p.*, u.username FROM posts p JOIN users u ON p.user_id = u.id ORDER BY p.created_at DESC'
        ).fetchall()
        return render_template('index.html', posts=posts, user=get_current_user())
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        db = get_db()
        
        # No validation for duplicate usernames or emails
        db.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, password)  # Intentionally storing password in plaintext
        )
        db.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',  # Vulnerable to SQL injection
            (username, password)
        ).fetchone()
        
        if user:
            session['user_id'] = user['id']
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = get_current_user()
    return render_template('profile.html', user=user)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        
        user = get_current_user()
        
        if user['password'] == old_password:  # Insecure direct comparison
            db = get_db()
            db.execute(
                'UPDATE users SET password = ? WHERE id = ?',
                (new_password, user['id'])  # Still storing in plaintext
            )
            db.commit()
            flash('Password changed successfully!')
            return redirect(url_for('profile'))
        else:
            flash('Current password is incorrect.')
    
    return render_template('change_password.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        file = request.files['file']
        
        # If user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add timestamp to filename to avoid conflicts
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(file_path)
            
            db = get_db()
            db.execute(
                'INSERT INTO images (user_id, filename, path) VALUES (?, ?, ?)',
                (session['user_id'], filename, file_path)
            )
            db.commit()
            
            flash('File successfully uploaded')
            return redirect(url_for('gallery'))
    
    return render_template('upload.html')

@app.route('/gallery')
def gallery():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    db = get_db()
    user_id = session['user_id']
    images = db.execute(
        'SELECT * FROM images WHERE user_id = ? ORDER BY created_at DESC',
        (user_id,)
    ).fetchall()
    
    return render_template('gallery.html', images=images)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        content = request.form['content']
        user_id = session['user_id']
        
        db = get_db()
        db.execute(
            'INSERT INTO posts (user_id, content, created_at) VALUES (?, ?, ?)',
            (user_id, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        db.commit()
        
        flash('Post created successfully!')
        return redirect(url_for('index'))
    
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(ssl_context=('certs/server.crt', 'certs/server.key'), debug=True, host='0.0.0.0', port=8443)
