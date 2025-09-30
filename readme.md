##Business Management System API

TeaSync is a Django-based API management system designed for tea business operations, providing robust RESTful APIs to manage users, products, vendors, customers, sales, invoices, payments, and wholesale purchases. Built with Django REST Framework, it includes token-based authentication and a customized admin panel for efficient data management.
Features

##Robust RESTful APIs: Comprehensive endpoints for managing users, products, vendors, customers, sales, invoices, payments, and wholesale purchases, tested via Postman.
##Custom User Authentication: Custom User model with role-based access (admin/staff) and secure token-based authentication.
Inventory Management API: Endpoints for product data, including retail/wholesale pricing, stock quantities, and vendor associations, with full CRUD support.
##Sales and Financial APIs: APIs for sales transactions, invoice generation, and payment processing with real-time status tracking.
##Admin Panel Integration: Django admin interface with customized displays, filters, and search for managing API-driven models.
##Data Validation and Serialization: Django REST Framework serializers ensure robust data validation and consistent JSON responses.

##Prerequisites

Python 3.8+
Django 4.x
Django REST Framework
Postman (for API testing)
SQLite (default database)

##Setup Instructions

Clone the Repository:
git clone https://github.com/Tanjeem1/Buisness-management-system-API.git
cd management


##@Create a Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


##Install Dependencies:

pip install -r requirements.txt



##Apply Migrations:
python manage.py makemigrations core
python manage.py migrate


##Collect Static Files (for admin panel):
python manage.py collectstatic --noinput


##Run the Server:
python manage.py runserver



##API Testing with Postman
Setup Postman
##API DOCUMENTATION LINK: https://documenter.getpostman.com/view/39770088/2sB3QDvsw6


#Troubleshooting

401 Unauthorized: Re-run POST /api-token-auth/ for a valid token.
404 Not Found: Verify endpoint in core/api_urls.py.
400 Bad Request: Ensure JSON fields match serializers.py (e.g., role as "admin" or "staff").
Foreign Key Errors: Use valid IDs from GET responses.
Report issues with Postman response bodies.

