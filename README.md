# Flask Calculator App 🧮

A simple web-based calculator built with **Flask** (Python) and enhanced with HTML, CSS, and JavaScript. This project is part of an internship assignment focused on building a modular backend, adding a frontend, testing with `pytest`, and setting up a CI/CD pipeline using GitLab and Docker.

## 📁 Project Structure

```
flask-calculator/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── calculator.py
│   ├── static/
│   │   └── style.css
│   │   └── script.js
│   └── templates/
│       └── index.html
├── tests/
│   └── test_calculator.py
├── app.py
├── requirements.txt
├── README.md
```

## 🚀 Features

- Four basic operations: Addition, Subtraction, Multiplication, Division
- Division-by-zero handling
- Input validation
- Interactive frontend with HTML + CSS + JavaScript
- API-driven backend using Flask
- Unit testing with Pytest
- CI/CD integration (coming up in Task 1.2)

## 🔧 How to Run Locally

```bash
git clone https://gitlab.com/<your-username>/flask-calculator.git
cd flask-calculator
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## ✅ Testing

```bash
pytest
```

## 🛠️ Tech Stack

- Python 3.x
- Flask
- HTML, CSS, JS (Vanilla)
- Pytest
- GitLab CI/CD (upcoming)
- Docker (upcoming)