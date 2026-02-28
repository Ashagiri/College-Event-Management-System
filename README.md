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
**Core**: Python 3.14, Django 6.0.2

**Database**: SQLite (ACID compliant)

**Frontend**: Bootstrap 5, Custom CSS3

**Environment**: Virtualenv for dependency isolation

# 📸 Screenshots
<p align="center">
  <img width="1896" height="975" alt="image" src="https://github.com/user-attachments/assets/a588e182-8828-49f4-8b90-2b230b95c423" />
  <img width="1902" height="942" alt="image" src="https://github.com/user-attachments/assets/0c1086f2-4190-4ddf-abd8-bcc8fe32c10f" />
  <img width="1902" height="938" alt="image" src="https://github.com/user-attachments/assets/98437630-930b-4b1b-8177-1384feb1430c" />
  <img width="1672" height="985" alt="image" src="https://github.com/user-attachments/assets/55cd1b25-0857-4f05-bae1-ffe60a9a5516" />
  <img width="1898" height="996" alt="image" src="https://github.com/user-attachments/assets/7daf2e4b-99dd-4f8c-85e9-fab2c265d5c5" />
  <img width="1896" height="943" alt="image" src="https://github.com/user-attachments/assets/04593427-4a9b-4210-b9ef-28381079c74c" />
</p>

# ⚙️ Installation & Setup
Clone the Repository

Bash
git clone https://github.com/Ashagiri/College-Event-Management-System.git
cd College-Event-Management-System
Initialize Environment

Bash
python -m venv env
.\env\Scripts\activate  # Windows
Install Requirements

Bash
pip install -r requirements.txt
Database Migration & Launch

Bash
python manage.py migrate
python manage.py runserver

# 🏁 Conclusion
By following this procedure, visitors can establish a clean development environment for the College Event Management System. This setup ensures that the Django application runs smoothly and securely on any local machine.
This system solves the "mess" of unmanaged event registration by providing a digital gateway for students. Future updates will include automated email notifications and certificate generation.


