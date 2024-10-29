# Django Project with Docker and PostgreSQL

This project runs a Django web application using Docker and PostgreSQL.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Project Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/ashcode002x/quiz/
    cd quiz
    ```

2. Create a `.env` file in the root directory to store your environment variables (optional but recommended).

    ```plaintext
    POSTGRES_DB=quiz_db
    POSTGRES_USER=aashi
    POSTGRES_PASSWORD=1234
    ```

3. Update your Django settings to connect to PostgreSQL. In `settings.py`, replace the default database configuration with:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'quiz_db',
            'USER': 'aashi',
            'PASSWORD': '1234',
            'HOST': 'db',  # Database service name in docker-compose
            'PORT': '5432',
        }
    }
    ```

## Running the Project with Docker

### Step 1: Build and Run Docker Containers

1. Build and start the containers using Docker Compose:
    ```bash
    docker-compose up --build
    ```

2. This will do the following:
   - Set up a PostgreSQL database container with the configurations provided.
   - Set up a Django web container and start the development server.

3. You should see your Django application running at `http://localhost:8000`.

### Step 2: Apply Migrations and Create a Superuser

1. After starting the containers, open a new terminal window and run the following commands to apply migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

2. Create a superuser to access the Django admin:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

### Step 3: Load Initial Data (Optional)

If you have data in a JSON file (e.g., `data.json`), you can load it into PostgreSQL:

```bash
docker-compose exec web python manage.py loaddata data.json
