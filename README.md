# Food Menu App - Django Project

## Project Overview
The Food Menu App is a web application built using the Django framework. This project provides functionality for managing a food menu, including adding, editing, and deleting items, viewing details, user authentication, and profile management. It’s designed to demonstrate the core features of Django, such as views, models, templates, static files, and more.
---
## Key Features

### 1.*Dynamic Food Menu:*
- Add, edit, view, and delete food items with descriptions, prices, and images.

### 2. *User Authentication:*
- Register, log in, log out, and manage user accounts.

### 3.*Responsive Design:*
- A user-friendly and responsive interface, optimized for different devices.
### 4. *Detail View for Items:*
-Detailed pages for each menu item with relevant information.

### 5.*Admin Panel Integration:*
-Utilize the Django Admin Panel to manage users and menu items easily.

### 6. *Profile Management:*
-Support for user profiles, including profile pictures and additional information.

### 7. *Static and Media Files:*
-Proper management of static files (CSS, JS) and media files (images).

### 8. *Customizable Navbar:*
-A navigation bar dynamically changes based on user authentication status.

### 9. *Class-Based and Function-Based Views:*
-Implementation of both view types to demonstrate Django's flexibility.

### 10.*Django Signals:*
- Use signals to handle specific tasks like associating users with posts automatically.
---

## Setup Instructions

1. Clone the Repository
   
git clone https://github.com/your-username/food-menu-app.git
cd food-menu-app

2. Install Dependencies

pip install -r requirements.txt

3. Run Migrations
   
python manage.py makemigrations
python manage.py migrate

4. Create a Superuser

python manage.py createsuperuser

6. Run the Development Server

python manage.py runserver

7. Access the App
Open your browser and go to:
http://127.0.0.1:8000
---

## How It Works
- Views and Templates: Handles the user interface and logic for displaying content.
- Models: Defines the database structure for menu items, user profiles, and more.
- URL Patterns: Routes requests to appropriate views.
- Static and Media Files: Manages CSS, JS, and uploaded images.
---
## Technologies Used
- *Backend:*  Django (Python)
- *Frontend:* HTML, CSS (Bootstrap), JavaScript
- *Database:* SQLite 
---

## Learning Highlights

## This project covers:

- Setting up a Django project
- Building models and working with databases
- Using Django templates and static files
- Adding forms and validations
- Implementing user authentication and authorization
- Using Django signals for automation
- Enhancing designs for a polished look
---

## Future Enhancements
- Add search functionality for food items.
- Include user roles for admin and customers.
- Integrate a payment gateway for ordering food items.

