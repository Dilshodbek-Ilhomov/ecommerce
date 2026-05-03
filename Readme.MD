# 🛒 E-Commerce API Platform

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![DRF](https://img.shields.io/badge/rest_framework-3.14-red.svg)
![Celery](https://img.shields.io/badge/celery-5.3+-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

A powerful, scalable, and feature-rich E-Commerce API platform built with **Django** and **Django REST Framework**. This project provides a complete backend solution for modern online stores, including background task processing, automated notifications, and secure authentication.

---

## 🌟 Key Features

- **Secure SMS Authentication**: OTP-based login system using Infobip.
- **Thread-Safe Order Management**: Atomic transactions and `F()` expressions prevent race conditions in stock management.
- **Product Management**: Categorized products with stock tracking and replenish alerts.
- **Flash Sales**: Dynamic discount management for specific time intervals.
- **Background Tasks**: Celery-powered worker for sending emails and Telegram notifications.
- **API Documentation**: Fully documented using Swagger UI and ReDoc.

---

## 🚀 Tech Stack

- **Framework:** Django 4.2+, DRF
- **Auth:** JWT (SimpleJWT) + Custom SMS OTP
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
   
   # SMS Auth (Infobip)
   SMS_KEY='App your_infobip_api_key'
   SMS_URL='https://your_infobip_api_url'
   
   # Notifications
   TELEGRAM_BOT_TOKEN='your-bot-token'
   CHAT_ID='your-telegram-chat-id'
   
   # Task Queue
   CELERY_BROKER_URL='amqp://guest:guest@rabbitmq:5672//'
   CELERY_RESULT_BACKEND='redis://redis:6379/0'
   ```

3. **Build and Run:**
   ```bash
   docker-compose up --build
   ```

4. **Initialize Database:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

---

### Manual Installation (Local)

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations custom_auth
   python manage.py migrate
   ```

4. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```

---

## 📂 Project Structure

```text
ecommerce/
├── config/             # Core settings and URL routing
├── products/           # Product and Order management logic
│   ├── models/         # Database schemas (Product, Order, FlashSale)
│   ├── views/          # API controllers
│   ├── serializers/    # Data transformation and validation (Atomic updates)
│   ├── signals.py      # Event triggers
│   └── tasks.py        # Background tasks (Celery)
├── custom_auth/        # SMS OTP Authentication system
├── billing/            # Payment integration (Stripe)
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-container orchestration
├── .env                # Environment configuration
└── requirements.txt    # Project dependencies
```

---

## 👨🏻‍💻 Author
**Dilshodbek Ilhomov** - [GitHub](https://github.com/Dilshodbek-Ilhomov)
