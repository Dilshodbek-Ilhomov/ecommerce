# 🛒 E-Commerce API Platform

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![DRF](https://img.shields.io/badge/rest_framework-3.14-red.svg)
![Celery](https://img.shields.io/badge/celery-5.3+-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

A powerful, scalable, and feature-rich E-Commerce API platform built with **Django** and **Django REST Framework**. This project provides a complete backend solution for modern online stores, including background task processing and automated notifications.

---

## 🚀 Tech Stack

- **Framework:** Django 4.2+, DRF
- **Task Queue:** Celery 5.3+
- **Brokers:** RabbitMQ (Task Broker), Redis (Result Backend)
- **Database:** SQLite (Development) / PostgreSQL compatible
- **API Documentation:** Swagger UI (drf-yasg)
- **Environment:** Docker & Docker Compose

---

## 🛠 Installation & Setup

### Using Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dilshodbek-Ilhomov/ecommerce.git
   cd ecommerce
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY='your-secret-key'
   DEBUG=True
   TELEGRAM_BOT_TOKEN='your-bot-token'
   CHAT_ID='your-telegram-chat-id'
   CELERY_BROKER_URL='amqp://guest:guest@rabbitmq:5672//'
   CELERY_RESULT_BACKEND='redis://redis:6379/0'
   ```

3. **Build and Run:**
   ```bash
   docker-compose up --build
   ```
   The API will be available at [http://localhost:8000/](http://localhost:8000/).

---

### Manual Installation (Local)

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```
   *Note: For Celery features, you need to have RabbitMQ and Redis running locally.*

---

## 📖 API Documentation

The project includes interactive API documentation:

*   **Swagger UI:** [http://localhost:8000/](http://localhost:8000/)
*   **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 📂 Project Structure

```text
ecommerce/
├── config/             # Core settings and URL routing
├── products/           # Main application logic
│   ├── models/         # Database schemas
│   ├── views/          # API controllers
│   ├── serializers/    # Data transformation logic
│   ├── signals.py      # Event triggers (e.g., Order -> Telegram)
│   └── tasks.py        # Background tasks (Celery)
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-container orchestration
├── .env                # Environment configuration
└── requirements.txt    # Project dependencies
```

---

## 👨🏻‍💻 Author
**Dilshodbek Ilhomov** - [GitHub](https://github.com/Dilshodbek-Ilhomov)
