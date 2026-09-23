# 🛍️ Wonder — Full-Stack E-Commerce Platform

**Wonder** is a complete, production-deployed e-commerce web application built from scratch with Django. It handles the full retail flow — browsing, cart, checkout, real payment gateway integration, and order tracking — backed by a PostgreSQL database and cloud media storage.

**🔗 Live Demo:** [wonder-ecommerce.onrender.com](https://wonder-ecommerce.onrender.com)
**💻 Source Code:** [github.com/Saikiran58ravula/wonder-ecommerce](https://github.com/Saikiran58ravula/wonder-ecommerce)

> Note: hosted on a free-tier instance, so the first request after a period of inactivity may take 30–60 seconds while the server wakes up.

---

## ✨ Features

- **Product catalog** — 120+ products across 10+ categories, with category filtering and search across product name, description, and category
- **Persistent shopping cart** — works for guest visitors (session-based) and logged-in users, with automatic cart merging on login
- **User authentication** — registration, login, logout, and profile, built on Django's auth system with an auto-created user profile
- **Checkout & payments** — real Razorpay payment gateway integration (test mode) with server-side signature verification before an order is ever marked paid
- **Order tracking** — a visual status timeline (Placed → Paid → Shipped → Delivered) on the order confirmation and history pages
- **Admin dashboard** — customized Django admin with bulk actions for shipping/cancelling orders, inline order items, and stock management
- **Cloud media storage** — product images served via Cloudinary, not local disk, so they persist across deployments
- **Responsive design** — custom CSS grid layout, mobile-friendly, no framework dependency

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.1 (Python) |
| Database | PostgreSQL (production), SQLite (local dev) |
| Payments | Razorpay API |
| Media storage | Cloudinary |
| Static files | WhiteNoise |
| Deployment | Render |
| Frontend | Django Templates, custom CSS (no framework) |

---

## 📐 Architecture

The project is split into four Django apps, each owning a clear slice of the domain:

- **`products`** — catalog, categories, search
- **`cart`** — session/user cart logic, cart merging
- **`accounts`** — registration, login, profile
- **`orders`** — checkout, Razorpay integration, order tracking

---

## 🚀 Getting Started Locally

```bash
# Clone the repo
git clone https://github.com/Saikiran58ravula/wonder-ecommerce.git
cd wonder-ecommerce

# Set up a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create a .env file in the project root with:
#   SECRET_KEY=your-secret-key
#   DEBUG=True
#   ALLOWED_HOSTS=127.0.0.1,localhost
#   RAZORPAY_KEY_ID=your-razorpay-test-key
#   RAZORPAY_KEY_SECRET=your-razorpay-test-secret
#   CLOUDINARY_CLOUD_NAME=your-cloud-name
#   CLOUDINARY_API_KEY=your-api-key
#   CLOUDINARY_API_SECRET=your-api-secret

# Run migrations and start the server
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🧪 Testing Payments

The live demo uses Razorpay's **test mode** — no real money is processed. Use these test credentials at checkout:

- **Card:** `5267 3181 8797 5449`, any future expiry, any CVV
- **Netbanking:** select any bank → choose "Success" on the mock bank page

---

## 📌 Notes

- This project intentionally runs on free-tier infrastructure (Render + PostgreSQL free tier), which means the database and instance may sleep or reset periodically — appropriate for a portfolio/demo deployment, not production traffic.
- Razorpay is integrated in test mode; going live would require completed KYC/business verification, which is out of scope for a demo project.

---

## 👤 Author

**Saikiran Ravula (Sunny)**
B.Tech Computer Science Engineering (Data Science), 2026

- 💼 LinkedIn: [linkedin.com/in/saikiran-ravula1](https://linkedin.com/in/saikiran-ravula1)
- 💻 GitHub: [github.com/Saikiran58ravula](https://github.com/Saikiran58ravula)
- 🌐 Portfolio: [saikiran58ravula.github.io/portfolio-website](https://saikiran58ravula.github.io/portfolio-website)
- 📧 Email: saikiransunny58@gmail.com
