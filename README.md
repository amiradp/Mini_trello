# 🗂️ Mini Trello – Django Project Manager

A minimal Trello-like task management app built with Django.  
This project allows users to create and manage projects, add tasks with deadlines, track task statuses, and securely manage their own workspace.

---

## 🚀 Features

- 🔐 User authentication using `django-allauth`
- 👤 Custom user model
- 📁 Project & Task management
- ✅ Task status updates (TODO / IN_PROGRESS / DONE)
- 📆 Task deadlines
- 🔒 Per-user access control (each user sees only their own projects/tasks)
- ⚙️ Admin panel customization
- 🧩 Clean, reusable Django template structure

---

## 🧰 Built With

- Python 3.x  
- Django  
- Django Allauth  
- SQLite (development)  
- HTML / CSS  
- Git & GitHub

---

## 📸 Screenshots

> *(Add screenshots here later if you want to showcase the UI)*

---

## 🛠️ Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/mini-trello.git
cd mini-trello


2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt



4. Apply migrations and create superuser:
python manage.py migrate
python manage.py createsuperuser


5. Run the development server:
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.


🧪 Testing (optional)
You can add and run unit tests using Django's test framework:
python manage.py test


📌 Roadmap
 User authentication with django-allauth

 Project/task models

 CRUD views for tasks

 Access control

 UI Styling with Bootstrap

 Unit tests

 Deployment to production

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Django documentation

Trello for design inspiration

Django Allauth

