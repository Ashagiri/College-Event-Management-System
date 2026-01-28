# 🎓 College-Event-Management-System

A robust web application built using the **Django framework**, designed to streamline the organization and registration process for campus events.

## 🚀 Key Features
* **Real-time Capacity Tracking:** Automatically calculates available seats to prevent over-booking.
* **Secure Authentication:** Separate portals for Students and Administrators using Django's built-in security.
* **Event Discovery:** A searchable dashboard for students to find upcoming fests and workshops.
* **Admin Dashboard:** A centralized interface for staff to manage event details and monitor participation.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap
* **Database:** SQLite (Development)

## 📸 Screenshots
<p align="center">
  <img src="assets/image.png" width="400" alt="Dashboard Overview">
  <img src="assets/image-1.png" width="400" alt="Event Details">
</p>

## 🧪 Testing
To ensure the system is running correctly, follow these steps:
1. **Server Check:** Run `python manage.py runserver` to ensure the server starts.
2. **Database:** Run `python manage.py migrate` to verify all tables are created.
3. **Functional Test:** Create a test event in the `/admin` panel and register as a student to check capacity updates.

## 🏁 Conclusion
This system solves the "mess" of unmanaged event registration by providing a digital gateway for students. Future updates will include automated email notifications and certificate generation.



