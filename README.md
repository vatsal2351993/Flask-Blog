# Blog Website

A fully functional blog website built using Flask and JavaScript, featuring user authentication, profile management, comment functionality, and advanced features like image uploads, SMTP-based password recovery, and custom error handling pages.

---

## Features

### User Management
- **User Registration**: Create a new account with secure password hashing (Flask-Bcrypt).
- **User Login**: Authenticate securely using Flask-Login.
- **Forgot Password**: Reset your password using SMTP email verification.
- **Profile Management**: Update profile information, including uploading a profile picture.

### Blog Management
- **Post Creation**: Create and manage blog posts with optional image uploads.
- **Comment System**: Add, view, and manage comments on blog posts.
- **Categories**: Categorize posts for easier navigation.

### Advanced Features
- **Image Uploads**: Upload and manage images for profiles and posts using Pillow.
- **Error Handling**: Custom error pages for 403, 404, and 500 errors.
- **Database Management**: SQLAlchemy integration for handling users, posts, comments, and image metadata.
- **Caching Control**: Prevent browser caching issues with appropriate HTTP headers.
- **JavaScript Interactivity**: Client-side interactivity for forms, dynamic content updates, and AJAX requests.
- **Deployment-Ready**: Configured for production using Gunicorn.

---

## Tech Stack

### Backend
- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: For database ORM.
- **Flask-Login**: For user session management.
- **Flask-Bcrypt**: For secure password hashing.
- **Flask-Mail**: For handling email functionality (SMTP).
- **Flask-WTF**: For secure form handling.

### Frontend
- **Jinja2**: For server-side templating.
- **HTML/CSS**: For static content and styling.
- **JavaScript**: For client-side interactivity and AJAX.

### Database
- **SQLAlchemy**: Used with a PostgreSQL database.

### Dependencies

```plaintext
bcrypt==4.2.1
blinker==1.9.0
click==8.1.8
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
Flask==3.1.0
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-Mail==0.10.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
gunicorn==23.0.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
MarkupSafe==3.0.2
packaging==24.2
pillow==11.1.0
psycopg2==2.9.10
python-dotenv==1.0.1
SQLAlchemy==2.0.37
typing_extensions==4.12.2
Werkzeug==3.1.3
WTForms==3.2.1
```

---

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- A Gmail account for SMTP email functionality.
- A browser supporting modern JavaScript features.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the project root with the following:
   ```env
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/db_name
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_password
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the development server:
   ```bash
   flask run
   ```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

### Setting Up the Admin
- Register a user on the site.
- Use Flask-Shell to promote the user to an admin:
  ```bash
  flask shell
  >>> from blog.models import User
  >>> user = User.query.first()
  >>> user.is_admin = True
  >>> db.session.commit()
  ```

### Sending Emails
Ensure that your SMTP credentials are valid and allow for less secure app access (or use App Passwords).

---

## Custom Error Pages

### 403 Error Page
A page is displayed when the user attempts to access a resource they are not authorized to view.

### 404 Error Page
A user-friendly page is displayed when a requested resource is not found.

### 500 Error Page
An informative page is displayed when the server encounters an error, with details logged for debugging.

---

## JavaScript Features

### Form Validation
- Client-side validation for user input before submission.

### Dynamic Content Loading
- Use of AJAX to dynamically load comments and posts without reloading the page.

### Interactive Features
- Profile picture previews before upload.
- Real-time comment updates.

---

## Deployment

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run the app with Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
   ```

3. Use a reverse proxy (e.g., Nginx) for production deployment.

---

## License
This project is licensed under the MIT License.

---

## Contributions
Feel free to fork the repository and submit pull requests. Contributions are welcome!
