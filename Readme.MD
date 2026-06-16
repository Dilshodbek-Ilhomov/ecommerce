# 🛒 E-Commerce API

A clean, scalable, and feature-rich E-Commerce API platform built with **Django** and **Django REST Framework**.

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/Dilshodbek-Ilhomov/ecommerce.git
cd ecommerce


# Run with Docker
docker-compose up --build
```

> [!NOTE]
> Create a `.env` file in the root directory based on the project requirements (SMS keys, Telegram tokens, etc.) before running in production.

---

## 🚀 Tech Stack

- **Core:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT) & Custom SMS OTP (Infobip)
- **Async Tasks:** Celery, RabbitMQ, Redis
- **Documentation:** Swagger UI (drf-yasg)

---

## 🌟 Key Features

- **Race Condition Prevention:** Atomic transactions for stock management.
- **Background Tasks:** Email and Telegram notifications via Celery.
- **Secure Auth:** SMS OTP-based login system.
- **Dockerized:** Ready for development and production.

---

## 👨🏻‍💻 Author
**Dilshodbek Ilhomov** - [GitHub](https://github.com/Dilshodbek-Ilhomov)
