# TransportSimple

A full-stack Django-based clone of Quora where users can register, post questions, answer them, like/dislike answers, and more. The project focuses on clean functionality and a polished user interface using HTML, CSS, and JavaScript.

---

## 🚀 Features

- ✅ User Registration & Login (with CSRF protection)
- 📝 Post Questions and Answers
- ❤️ Like & Dislike Answers (sorted by likes)
- 🔐 Django Auth System Integrated
- 🎨 Custom Styling for Forms and Navigation
- 📋 Django Forms with Error Handling
- 📊 Sorted answer display for better UX

---

## 📸 Screenshots

*(Add your screenshots here, like login page, question list, etc.)*

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3 (default, easily switchable to MySQL/PostgreSQL)
- **Templating:** Django Templating Engine (Jinja-style)

---

## 🏗 Project Setup

Follow these steps to run the project locally:

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/quora-clone-django.git
cd quora-clone-django

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
