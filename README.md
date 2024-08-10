# To Do List 📝

## 🧪Demo
<p align="center">
  <img src="https://github.com/user-attachments/assets/d9965bcb-0746-467c-871f-66de78935afd" alt="Demo">
</p>

## 📝Content

- [Overview](#%EF%B8%8Foverview)
- [Technologies](#technologies)
- [Features](#features)
- [Project Structure](#%EF%B8%8Fproject-structure)
- [Run Project](#run-project)
- [Contributing](#contributing)
- [Contact](#contact)

## 🗺️Overview

The To Do List app is a simple web application designed to help users manage their daily tasks efficiently. It allows users to add, delete, and mark tasks as completed.

## 👨‍💻Technologies

- **Flask**: A lightweight WSGI web application framework.
- **HTML/CSS**: For building and styling the web interface.
- **Flask-SQLAlchemy**: ORM library for Flask to interact with the database.
- **SQLite**: Database to store todo tasks.

## 👀Features

- **Add Tasks**: Users can add new tasks to their to-do list.
- **Delete Tasks**: Users can remove tasks they no longer need.
- **Mark as Completed**: Users can mark tasks as completed.

## 🗃️Project Structure

- `/instance`
  - `todo.db`: SQLite database file containing the tasks.
- `/templates`
  - `index.html`: HTML template for the main interface.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `app.py`: Main Flask application script.
- `requirements.txt`: Required libraries for running the project.

## ✅Run Project

1. **Clone the repository**:
```
git clone https://github.com/buroff1/todo_list-website.git
cd todo_list-website
```
2. **Set up a virtual environment**:
```
python3 -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
3. **Install dependencies**:
```
pip install -r requirements.txt
```
4. **Initialize the database**:
```
flask db upgrade
```
5. **Run the application**:
```
flask run
```
6. **Visit the website**:
Open `http://localhost:5000` in your web browser.

## 🤝Contributing

Interested in contributing? Follow these steps:

1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📧Contact

- Email: [artem.burov0205@gmail.com](mailto:artem.burov0205@gmail.com)
- GitHub: [buroff1](https://github.com/buroff1)
