# Django Blog Project

This Django blog project is a simple web application built using Django, a high-level Python web framework. It allows users to create, edit, and delete blog posts, as well as comment on existing posts.

## Features

- User authentication: Users can register, log in, and log out.
- CRUD operations on blog posts: SuperUsers can create, read, update, and delete blog posts.
- Commenting system: Users can leave comments on blog posts.
- Responsive design: The blog is designed to be mobile-friendly.

## Installation

1. Clone the repository:

git clone https://github.com/your_username/django-blog.git

2. Navigate to the project directory:

cd web_blog

3. Install dependencies:

pip install -r requirements.txt

4. Apply database migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver

6. Access the blog in your web browser at http://localhost:8000.

## Usage

- You can create a superuser account to access the Django admin interface:

python manage.py createsuperuser

default superuser is:
username - admin
password - admin

- Log in to the admin interface at http://localhost:8000/admin to manage blog posts and comments.

## Credits

- This project was created by Albert D.

