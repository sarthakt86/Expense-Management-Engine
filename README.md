# 💰 Expense Management Engine

A simple **Expense Management Web Application** built using **Python Flask**.
This project was originally a **CLI-based expense tracker** and later converted into a **Flask Web Application**.

---

## 🚀 Features

* Add new expenses
* View expense history
* Data stored in JSON file
* Lightweight Flask backend
* Simple web interface

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML
* Bootstrap
* JSON (for data storage)

---

## 📂 Project Structure

```
Expense-Management-Engine
│
├── app.py
├── main.py
├── expenses.json
├── requirements.txt
├── Dockerfile
│
├── templates
│   ├── index.html
│   ├── add_expense.html
│   └── view_expenses.html
│
└── README.md
```

---

## ▶️ Run Locally

### Clone the repository

```
git clone https://github.com/sarthakt86/Expense-Management-Engine.git
```

### Go to project folder

```
cd Expense-Management-Engine
```

### Install dependencies

```
pip install flask
```

### Run the application

```
python app.py
```

### Open in browser

```
http://127.0.0.1:5000
```

---

## 🐳 Docker Support

Build Docker image

```
docker build -t expense-app .
```

Run container

```
docker run -p 5000:5000 expense-app
```

---

## ☁️ Deployment (AWS)

This project can be deployed using:

* Docker
* AWS EC2
* DockerHub

Deployment architecture:

```
Local Machine
      │
Docker Image
      │
DockerHub
      │
AWS EC2
      │
Flask Web App (Live)
```

---

## 📌 Future Improvements

* Better UI with Bootstrap
* Expense categories filtering
* Database integration (MySQL / PostgreSQL)
* Authentication system
* Dashboard with charts

---

## 👨‍💻 Author

**Sarthak Tiwari**

GitHub:
https://github.com/sarthakt86
