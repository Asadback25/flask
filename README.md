# Fibonacci Calculator

A simple, elegant web application built with **Flask (Python)** for the backend and **HTML, CSS, JavaScript** for the frontend. This tool allows you to calculate Fibonacci numbers step by step with a clear explanation of how each number in the sequence is derived.

---

## ✨ Features

* 🔢 **Fibonacci calculation** with step-by-step explanation.
* 🎨 **Modern UI** with gradients, shadows, and smooth interactions.
* 🖥️ **Responsive design** optimized for desktop.
* 📖 **Info modal** explaining the purpose of the tool.
* ❌ **Error handling** for invalid inputs.

---

## 🚀 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Fonts & Styles:** Google Fonts (Rubik)

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/asadback25/flask.git
cd flask
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Open in browser

Navigate to:

```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
fibonacci-calculator/
│
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend UI
└── README.md           # Project documentation
```

---

## 🧮 Example Output

For input `5`, the app will show:

```
F(5) = 5

How was it calculated?
F(0) = 0
F(1) = 1
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
```

---

## 🌍 Open Source

This project is **open source** and available for everyone to use, modify, and improve. Contributions are welcome!

---

## 👨‍💻 Author

Developed with ❤️ by **To'rayev Asadbek**

📧 Feel free to connect and contribute!
