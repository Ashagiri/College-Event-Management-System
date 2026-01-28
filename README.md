# College-Event-Management-System
# 📌 Introduction:
The College Event Management System is a robust web application built using the Django framework, designed to streamline the organization and registration process for campus events.

In many colleges, event registration is often unmanaged, leading to overcrowded venues and a poor experience for attendees. 
This project specifically addresses that "mess" by implementing a Dynamic Capacity Control system. By linking registrations directly to available seats, the system ensures that every event remains organized, safe, and professional.

# 🚀 Key Features
Real-time Capacity Tracking: Automatically calculates "Filled vs. Available" seats to prevent over-booking.

Secure Authentication: Separate portals for Students and Administrators using Django's built-in security.

Event Discovery: A searchable dashboard that allows students to find upcoming fests, workshops, and competitions.

MVT Architecture: Built using a clean Model-View-Template structure for high performance and scalability.

Admin Dashboard: A centralized interface for college staff to manage event details and monitor student participation.

# 🛠️ Tech Stack
Backend: Python, Django

Frontend: HTML5, CSS3, Bootstrap (Template Inheritance via base.html)

Database: SQLite (Development)

## 🧪 Testing
To ensure the system is running correctly, follow these steps:
* **Server Check:** Run `python manage.py runserver` and ensure the development server starts without errors.
* **Database Migrations:** Verify all tables are created by running `python manage.py migrate`.
* **Functional Testing:** * Register a new user and log in to the student portal.
    * As an Admin, create an event and check if the capacity decreases when a student registers.
* **UI Testing:** Ensure the dashboard is responsive on both mobile and desktop views.

---

## 🏁 Conclusion
The **College Event Management System** successfully solves the problem of unmanaged campus crowds by providing a digital gateway for event registration. By utilizing Django's robust backend and a clean MVT architecture, the system ensures data integrity and a smooth user experience. 

Future updates will include email notifications for successful registrations and an automated certificate generation system for attendees.







