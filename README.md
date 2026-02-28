# 🎓 College Event Management System
A high-performance, full-stack web application designed to digitize campus event workflows, from student registration to real-time seat management.

# 🌟 Overview
Traditional event management is often disorganized. This system provides a **centralized gateway** for students to discover workshops and fests while giving administrators powerful tools to track participation metrics.

# 🚀 Key Features
**Dynamic Event Dashboard** : Searchable and filterable interface for event discovery.

**Smart Capacity Logic**: Backend validation to prevent over-booking based on venue limits.

**Role-Based Access**: Specialized views for students (registrations) and administrators (event creation).

**Automated Media Handling**: Integrated image processing for event banners using Pillow.

# 🛠️ Tech Stack
Core: Python 3.14, Django 6.0.2

Database: SQLite (ACID compliant)

Frontend: Bootstrap 5, Custom CSS3

Environment: Virtualenv for dependency isolation
# 📸 Screenshots
<p align="center">
  <img width="1896" height="975" alt="image" src="https://github.com/user-attachments/assets/a588e182-8828-49f4-8b90-2b230b95c423" />
  <img width="1902" height="942" alt="image" src="https://github.com/user-attachments/assets/0c1086f2-4190-4ddf-abd8-bcc8fe32c10f" />
  <img width="1902" height="938" alt="image" src="https://github.com/user-attachments/assets/98437630-930b-4b1b-8177-1384feb1430c" />
  <img width="1672" height="985" alt="image" src="https://github.com/user-attachments/assets/55cd1b25-0857-4f05-bae1-ffe60a9a5516" />
  <img width="1898" height="996" alt="image" src="https://github.com/user-attachments/assets/7daf2e4b-99dd-4f8c-85e9-fab2c265d5c5" />
  <img width="1896" height="943" alt="image" src="https://github.com/user-attachments/assets/04593427-4a9b-4210-b9ef-28381079c74c" />
</p>

# 🧪 Testing
To ensure the system is running correctly, follow these steps:
1. **Server Check:** Run `python manage.py runserver` to ensure the server starts.
2. **Database:** Run `python manage.py migrate` to verify all tables are created.
3. **Functional Test:** Create a test event in the `/admin` panel and register as a student to check capacity updates.

# 🛠️ Environment Setup Procedure
Follow these steps to get the project running on your local machine:

## 1. Prerequisites
Ensure you have Python 3.8+ installed.

Ensure Git is installed and configured in your path.

## 2. Clone the Repository
Open your terminal and run:

git clone https://github.com/Ashagiri/College-Event-Management-System.git
cd your-repo-name
## 3. Create a Virtual Environment
It is highly recommended to use a virtual environment to keep dependencies isolated:

Bash
### Windows
python -m venv env

.\env\Scripts\activate

### macOS/Linux
python3 -m venv env
source env/bin/activate

## 4. Install Dependencies
Install the required packages (make sure you are in the same folder as manage.py):

Bash

pip install -r requirements.txt
## 5. Apply Migrations
Set up the database schema:

Bash
python manage.py migrate
## 6. Run the Application
Start the development server:

Bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to see the app live!


# 🏁 Conclusion
By following this procedure, visitors can establish a clean development environment for the College Event Management System. This setup ensures that the Django application runs smoothly and securely on any local machine.
This system solves the "mess" of unmanaged event registration by providing a digital gateway for students. Future updates will include automated email notifications and certificate generation.


