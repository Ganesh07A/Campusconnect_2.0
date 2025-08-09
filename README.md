# 📚 CampusConnect 2.0

**Connecting every corner of campus – smarter, faster, better.**

CampusConnect 2.0 is a modern college portal built with **Django** and **Bootstrap**, designed to centralize campus updates, events, and council information while providing a smooth user experience.

---

## 🚀 Features
- 🗓 **Event Management** – List upcoming events with images, speakers, and dates.
- 🏛 **Council Updates** – View council members and their activities.
- 📝 **Event Registration** – Register for events via a clean modal form (stores data in DB).
- 👤 **User Authentication** – Register and sign in with a separate `user` app.
- 📱 **Responsive UI** – Built with Bootstrap for mobile-friendly design.
- 🎨 **Clean Styling** – Transparent navbar, organized sections, and separate CSS.

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

**Campusconnect/**
│
├── council/                 # Council app
│   ├── migrations/          
│   ├── templates/council/   # Council-related HTML files
│   ├── static/council/      # Council-specific CSS/JS/images
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── forms.py
│
├── events/                  # Events app
│   ├── migrations/
│   ├── templates/events/    # Event listing & registration pages
│   ├── static/events/       # Event-specific CSS/JS/images
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── forms.py
│
├── users/                   # User authentication app
│   ├── migrations/
│   ├── templates/users/     # Login & register HTML
│   ├── static/users/        # User-related CSS/JS
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/                  # Global static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/               # Global templates
│   ├── base.html
│   ├── index.html
│   ├── navbar.html
│   ├── about.html
│   └── services.html
│
├── Campusconnect/        # Main project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│               
├── manage.py
└── README.md


 Developed by **Ganesh Suvarnakar** with **💖**
 
