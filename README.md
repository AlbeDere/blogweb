# Django Blog Project

This Django blog project is a simple web application built using Django, a high-level Python web framework. It allows users to create, edit, and delete blog posts, as well as comment on existing posts.

## Features

- User authentication: Users can register, log in, and log out.
- CRUD operations on blog posts: SuperUsers can create, read, update, and delete blog posts.
- Commenting system: Users can leave comments on blog posts.
- Responsive design: The blog is designed to be mobile-friendly.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/AlbeDere/web_blog.git
    ```

2. Install dependencies:

    ```bash
    cd web_blog
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

    Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Docker Setup

This project includes Docker configuration for easy deployment. Follow these steps to run the application in a Docker container:

1. Install Docker Desktop for your operating system: [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. Build the Docker image:

    ```bash
    docker-compose build
    ```

3. Start the Docker containers:

    ```bash
    docker-compose up -d
    ```

    Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Contributing

Contributions are welcome! Please follow these guidelines when contributing to the project:

- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make your changes
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature`)
- Create a new Pull Request

## Usage

- You can create a superuser account to access the Django admin interface:

python manage.py createsuperuser

default superuser is:
username - admin
password - admin



