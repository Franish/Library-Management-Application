# Library Management System

A simple web-based Library Management System built with Django. This system allows librarians to manage books, members, and borrowing activities efficiently.

## Features

- Add, update, delete, and list books
- Register and manage library members
- Issue and return books
- Track borrowing history
- Admin interface for easy management

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS (Django Templates)

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
Create a virtual environment (optional)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Create superuser (optional)

bash
Copy
Edit
python manage.py createsuperuser
Run the development server

bash
Copy
Edit
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/

Project Structure
csharp
Copy
Edit
library-management-system/
├── library/             # Main app
├── library_management/  # Project settings
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS)
├── db.sqlite3           # Default database
├── manage.py
└── requirements.txt
