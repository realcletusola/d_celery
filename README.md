## Introduction

This project illustrates how to decouple time-consuming tasks like sending emails from the main application flow by using Celery, a distributed task queue. With Celery, tasks such as email delivery can be processed asynchronously, improving the responsiveness and scalability of the Django application.

---

## Features

- User registration and login functionality.
- Sending welcome emails upon registration.
- Sending login notification emails.
- Asynchronous task handling with Celery.
- Redis as the message broker.

---

## Technologies Used

- Django
- Celery
- Flower
- Redis
- Python

---

## Installation and Setup

### Clone the Repository
```bash
$ git clone https://github.com/realcletusola/d_celery.git
$ cd d_celery
```

### Install Dependencies
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```

### Set Up Redis
1. Install Redis on your machine:
   - On Linux: Use your package manager (e.g., `sudo apt install redis`).
   - On macOS: `brew install redis`.
   - On Windows: Download from [Redis for Windows](https://github.com/microsoftarchive/redis/releases).
2. Start the Redis server:
   ```bash
   $ redis-server
   ```
   
### Apply Migrations
```bash
$ python manage.py migrate
```

---

## Running the Application

### Starting Redis
Ensure Redis is running:
```bash
$ redis-server
```

### Starting Celery
Run the Celery worker:
```bash
$ celery -A d_celery worker --loglevel=info
```
### View Tasks in Browser
Run Flower
```bash
$ celery -A d_celery flower 
```
Visit http://localhost:5555 to view tasks using flower 

### Running the Django Server
```bash
$ python manage.py runserver
```

---

## How It Works

### User Registration and Login Workflow
1. A user registers or logs in to the application.
2. Django triggers a Celery task to send an email.
3. The task is added to the Redis queue and processed by a Celery worker.
4. The user receives an email without blocking the registration or login process.

   

