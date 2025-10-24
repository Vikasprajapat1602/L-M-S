# Library Management System

The **Library Management System (L-M-S)** is a Django-based web application to manage library operations such as books, students, and issue/return tracking.  
It provides an admin interface to manage data and a simple frontend for users.

---

## Folder Structure

library_mgmt/
│
├── library/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   └── library/
│   │       ├── base.html
│   │       ├── books.html
│   │       ├── home.html
│   │       ├── issue_book.html
│   │       ├── issue_list.html
│   │       ├── return_book.html
│   │       └── students.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── library_mgmt/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements
├── .gitignore
├── venv/
└── README.md

---

## Features

- Student and book management
- Book issue/return functionality
- Admin interface for management
- Search and list views for books and students

---

## Setup & Installation

1. **Clone the repository**

    ```
    git clone https://github.com/Vikasprajapat1602/L-M-S.git
    cd library_mgmt
    ```

2. **Apply migrations:**

   ```
   python manage.py migrate
   ```
   
3. **Create superuser (optional, for admin access)**

    ```
    python manage.py createsuperuser
    ```

4. **Run Server**

    ```
    python manage.py runserver
    ```

---

## Usage

- Open http://127.0.0.1:8000/ in your browser.
- Admin interface: http://127.0.0.1:8000/admin/
- Use student and book modules as per navigation.
- Admin login required for full access to data management.
