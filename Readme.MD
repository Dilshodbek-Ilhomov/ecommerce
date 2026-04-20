# 🛒 E-Commerce API Platform

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![DRF](https://img.shields.io/badge/rest_framework-3.14-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Ushbu loyiha zamonaviy elektron tijorat platformasi uchun mo'ljallangan kuchli va kengayuvchan API tizimidir. Django va Django REST Framework yordamida qurilgan bo'lib, to'liq savdo siklini boshqarish imkonini beradi.

---

## ✨ Asosiy Imkoniyatlar (Features)

*   **📦 Mahsulotlar Boshqaruvi:** Kategoriyalar, mahsulotlar va ularning batafsil ma'lumotlari.
*   **⭐ Sharhlar va Reytinglar:** Mahsulotlarga sharhlar qoldirish va o'rtacha reyting hisoblash.
*   **⚡ Flash Sales:** Maxsus vaqtinchalik chegirmalar tizimi.
*   **🛒 Buyurtmalar Tizimi:** Savatcha va buyurtma berish jarayoni.
*   **👤 Foydalanuvchi Boshqaruvi:** Djoser va JWT yordamida autentifikatsiya (Login/Register).
*   **📊 Ko'rishlar Tarixi:** Foydalanuvchilar ko'rgan mahsulotlar tarixini saqlash.
*   **🛠 Ombor Boshqaruvi:** Mahsulotlar qoldig'ini (stock) nazorat qilish va to'ldirish.

---

## 🚀 Texnologik Stek (Tech Stack)

- **Backend:** Django 4.2+, DRF
- **Autentifikatsiya:** JWT (SimpleJWT), Djoser
- **Hujjatlashtirish:** Swagger, Redoc (drf-yasg)
- **Ma'lumotlar Bazasi:** SQLite (Development) / PostgreSQL (Production ready)
- **Muhit o'zgaruvchilari:** python-dotenv

---

## 🛠 O'rnatish va Ishga Tushirish (Installation)

### 1. Loyihani yuklab olish
```bash
git clone https://github.com/Dilshodbek-Ilhomov/ecommerce.git
cd ecommerce
```

### 2. Virtual muhitni sozlash
```bash
python -m venv .venv
# Windows uchun
.venv\Scripts\activate
# Linux/Mac uchun
source .venv/bin/activate
```

### 3. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. .env faylini sozlash
`.env` faylini yarating va quyidagi parametrlarni kiriting:
```env
SECRET_KEY=yoursecretkey
SECRET_KEY='django-insecure-...'
EMAIL_HOST_USER='your-email@gmail.com'
EMAIL_HOST_PASSWORD='your-app-password'
```

### 5. Migratsiyalarni bajarish va ishga tushirish
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📖 API Hujjatlari (API Documentation)

Loyiha interaktiv hujjatlarga ega:

*   **Swagger UI:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 💾 Ma'lumotlarni Boshqarish (Database Management)

Eski serverdan ma'lumotlarni ko'chirish:

```bash
# Ma'lumotlarni faylga saqlash
python manage.py dumpdata > data.json

# Bazani tozalash
python manage.py flush 

# Ma'lumotlarni yuklash
python manage.py loaddata data.json
```

---

## 📂 Loyiha Tuzilishi (Project Structure)

```text
ecommerce/
├── config/             # Asosiy sozlamalar (settings, urls)
├── products/           # Asosiy ilova (models, views, serializers)
│   ├── migrations/     # DB migratsiyalari
│   ├── models/         # Modellar (split by category)
│   ├── serializers/    # DRF Serializers
│   ├── services/       # Biznes logika (business logic)
│   └── views/          # API endpointlari
├── .env                # Maxfiy ma'lumotlar
├── manage.py           # Django boshqaruv skripti
└── requirements.txt    # Kerakli kutubxonalar
```

---
🤝 **Muallif:** [Dilshodbek Ilhomov](https://github.com/Dilshodbek-Ilhomov)
