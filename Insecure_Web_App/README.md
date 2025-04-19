# Insecure Web Application

This is a simple web application that allows users to register, log in, upload images, view their gallery, and create posts. It's intentionally designed with minimal security features for educational purposes.

## Features

- User registration and login
- User profile page with basic information
- Password change functionality
- Image upload capability
- User-specific image gallery
- Create text posts
- View all posts on the home page

## Installation and Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository or extract the files to your preferred location

2. Open a terminal and navigate to the project directory

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

5. Install the required packages:
   ```bash
   pip install flask flask-login werkzeug
   ```

6. Initialize the database:
   ```bash
   export FLASK_APP=app.py
   flask init-db
   ```

7. Run the application:
   ```bash
   python app.py
   ```

8. Access the application in your web browser at:
   ```
   http://127.0.0.1:5000
   ```

## Using the Application

1. Register a new account from the Register page
2. Log in with your credentials
3. Upload images from the Upload Image page
4. View your uploaded images in My Gallery
5. Create posts from the Create Post page
6. View all posts on the Home page
7. Change your password from the Change Password page
8. View your profile information from the Profile page

## Notes

- This application is intentionally designed with minimal security features for educational purposes.
- Do not use this application in a production environment.
- All uploaded files are stored in the `static/uploads` directory.
- User data is stored in an SQLite database file named `database.db`.

