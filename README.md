Employee Management System

A web-based Employee Management System built using Django and Python. The system allows authorized users to manage employee records through a simple and professional dashboard.

🚀 Features

- User authentication and login
- Employee management
- Add, edit and delete employees
- Employee profile management
- Department management
- Employee search
- Task management
- Leave management
- Profile management
- Responsive web interface
- PostgreSQL database integration
- Django ORM
- PDF report generation
- Excel import/export
- Pagination

🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- PostgreSQL
- Git & GitHub
- ReportLab
- OpenPyXL
- Pillow

📁 Main Modules

- "accounts" — User authentication
- "employees" — Employee management
- "leaves" — Leave management
- "profiles" — User profile management
- "tasks" — Task management

⚙️ Installation

1. Clone the repository

git clone https://github.com/Danish9850/EmployeeManagementSystem.git

2. Open the project folder

cd EmployeeManagementSystem

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Configure PostgreSQL

Create your PostgreSQL database and update the Django database settings according to your local PostgreSQL configuration.

7. Run migrations

python manage.py migrate

8. Start the development server

python manage.py runserver

9. Open the application

Open your browser and visit:

http://127.0.0.1:8000/

🔄 Project Flow

Browser
   ↓
urls.py
   ↓
views.py
   ↓
Django ORM
   ↓
PostgreSQL
   ↓
views.py
   ↓
HTML Templates
   ↓
Browser

👨‍💻 Author

Danish9850

GitHub: https://github.com/Danish9850