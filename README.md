# 🛒 CommerceCore — RESTful E-Commerce API

CommerceCore is a scalable RESTful E-Commerce backend API developed using Flask. The project provides secure user authentication, product management, shopping cart functionality, and order processing through modular REST APIs. The application is deployed on Render and documented using Swagger UI for interactive API testing.

The system follows a modular architecture using Flask Blueprints and SQLAlchemy ORM, making the project maintainable, scalable, and production-oriented. The backend supports JWT-based authentication, paginated product retrieval, automated product seeding, and interactive API documentation.

---

# 🚀 Features

- 🔐 JWT-based User Authentication
- 🛍️ Product Management APIs
- 🛒 Shopping Cart Functionality
- 📦 Order Management System
- 📄 Swagger API Documentation
- 📚 RESTful API Architecture
- ⚡ Server-side Pagination
- 🧩 Modular Flask Blueprint Structure
- 🗄️ SQLite Database Integration
- ☁️ Cloud Deployment on Render
- 🔄 Automated Product Seeding
- 🌐 CORS Enabled APIs

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Flask | Backend Framework |
| SQLAlchemy | ORM & Database Operations |
| SQLite | Database |
| Flasgger | Swagger Documentation |
| Gunicorn | Production Server |
| Postman | API Testing |
| Git & GitHub | Version Control |
| Render | Cloud Deployment |

---

# 📂 Project Modules

## 🔐 Authentication
- User Registration
- User Login
- JWT Token Generation

## 🛍️ Products
- Add Products
- Retrieve Products
- Product Pagination

## 🛒 Cart
- Add Items to Cart
- View User Cart

## 📦 Orders
- Place Orders
- Retrieve User Orders

---

# 📖 API Documentation

Swagger UI is integrated for interactive API testing.

## Swagger Endpoint

```bash
/apidocs
```

Example:

```bash
https://your-render-url.onrender.com/apidocs
```

---

# ⚙️ Project Architecture

```plaintext
Client / Frontend
        ↓
REST API Endpoints
        ↓
Flask Application
        ↓
SQLAlchemy ORM
        ↓
SQLite Database
```

---

# 📌 Key Backend Concepts Implemented

- RESTful API Design
- JWT Authentication
- Flask Blueprints
- Database ORM Mapping
- Pagination
- Modular Architecture
- Cloud Deployment
- Swagger Documentation
- API Testing
- Database Seeding

---

# ☁️ Deployment

The application is deployed using:

- Render
- Gunicorn

---

# 📈 Future Enhancements

- PostgreSQL Migration
- Payment Gateway Integration
- Role-Based Access Control
- Product Search & Filtering
- Wishlist Functionality
- Docker Containerization
- Email Notifications
- Order Tracking System
- Admin Dashboard
- CI/CD Pipeline

---

# 🎯 Project Goal

The primary objective of CommerceCore is to simulate a real-world e-commerce backend system using modern REST API development practices. The project demonstrates scalable backend architecture, secure authentication mechanisms, modular code organization, and cloud deployment workflows commonly used in production environments.

---

# 👨‍💻 Author

Developed by Vivek Raj using Python and Flask.
