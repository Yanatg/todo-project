# Todo Application

A simple web application built with Django for managing personal todo lists. Users can register, log in, add, view, update the status of, and delete their tasks. Features a two-column layout and user-specific task management.

Meet the site -> [https://todo-project-r2zu.onrender.com/](https://todo-project-r2zu.onrender.com/)

<img width="721" alt="image" src="https://github.com/user-attachments/assets/41265ecd-6a6e-44dd-8647-2b5280568fc8" />
<img width="724" alt="image" src="https://github.com/user-attachments/assets/fbc03b3c-fc63-4ace-84c7-9839f15374ce" />


## Features

* User Authentication (Signup, Login, Logout) using Django's built-in system.
* Add new todo items with a title and optional description.
* View a list of all pending and completed todo items specific to the logged-in user.
* Update todo status (Pending/Done) using a checkbox with automatic form submission.
* Delete todo items with a confirmation prompt.
* Responsive two-column layout on the main page (Add form on left, List on right).

## Tech Stack / Built With

* **Backend:** Python, Django
* **Database:** PostgreSQL (Production via Render), SQLite (Local Development)
* **Frontend:** HTML, CSS (Plain)
* **Deployment:** Render, Gunicorn (WSGI Server), Whitenoise (Static Files)
* **Database ORM:** Django ORM
* **Environment Variables:** python-dotenv (local), Render Environment Variables (production)
* **Database Connector:** psycopg2-binary
* **URL Parsing:** dj-database-url

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.9+
* pip (Python package installer)
* Git
* PostgreSQL (Optional - only if you want to run locally with Postgres instead of SQLite)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Yanatg/todo-project.git
    cd todo-project
    ```

2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    * Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    * **Edit the `.env` file:**
        * Generate a new Django secret key (you can use an online generator or run `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`) and replace the placeholder `SECRET_KEY`.
        * Keep `DEBUG=True` for local development.
        * `ALLOWED_HOSTS` is pre-filled for local use.
        * `CSRF_TRUSTED_ORIGINS` is pre-filled for local use.
        * Leave `DATABASE_URL` commented out to use the default SQLite database, or uncomment and set it if you have a local PostgreSQL instance you want to use (e.g., `DATABASE_URL=postgres://user:password@localhost:5432/mydatabase`).

5.  **Apply Database Migrations:**
    * This will create the necessary database tables (either in `db.sqlite3` or your local Postgres).
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional):**
    * Allows access to the Django admin interface (`/admin/`).
    ```bash
    python manage.py createsuperuser
    ```
    * Follow the prompts to create an admin account.

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    * The application should now be running at `http://127.0.0.1:8000/`.

## `.env.example` File

Create a file named `.env.example` in the root directory with the following content to guide local setup:

```dotenv
# Example environment variables for local development
# Copy this to .env and fill in values. Add .env to .gitignore!

# Generate your own secret key for the .env file
SECRET_KEY='your_local_development_secret_key_here'

# Debug mode for local development
DEBUG=True

# Allowed hosts for local development server
ALLOWED_HOSTS=127.0.0.1,localhost

# Leave DATABASE_URL commented out to use default SQLite specified in settings.py
# Or uncomment and set if using local PostgreSQL:
# DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME

# CSRF Trusted origins for local development server
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

# Optional Security Headers (generally False for local HTTP)
# SECURE_SSL_REDIRECT=False
# SESSION_COOKIE_SECURE=False
# CSRF_COOKIE_SECURE=False
# SECURE_HSTS_SECONDS=0
