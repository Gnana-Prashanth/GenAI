<<<<<<< HEAD
# 🤖 AI Chatbot Web Application

**Think Champ PVT LTD – Internship Mini Project**

A simple AI-powered chatbot built with **Python**, **Flask**, and **Machine Learning** concepts. Users interact through a web interface that accepts messages and returns intelligent, dynamic responses.

---

## 📁 Project Structure

```
AI_Chatbot/
├── app.py              # Flask backend – routes & API
├── chatbot.py          # ML/NLP response logic
├── responses.json      # Knowledge base (patterns & responses)
├── templates/
│   └── index.html      # Frontend chat UI
├── static/
│   └── style.css       # Styling
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Install dependencies
```bash
pip install flask
```

### 3. Run the app
```bash
cd AI_Chatbot
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 🚀 Features

### Mandatory
- ✅ Welcome Page
- ✅ Chat Interface
- ✅ User Message Input
- ✅ AI Response Generation (pattern-matching ML logic)
- ✅ Flask Backend Integration
- ✅ Dynamic Chat Display
- ✅ Attractive User Interface (dark theme, animations)
- ✅ Multiple User Queries Handling

### Optional (implemented)
- ✅ Real-Time Responses (typing animation)
- ✅ Responsive Design

---

## 🧠 How It Works

1. User types a message in the browser
2. The frontend sends a `POST /chat` request with `{ "message": "..." }`
3. Flask receives the request and calls `chatbot.py`
4. `chatbot.py` preprocesses the input (lowercase, remove punctuation)
5. Pattern matching scores each knowledge category against the input
6. The best-matching response is randomly selected and returned as JSON
7. The frontend displays the response with a typing animation

---

## 📚 Topics the Bot Knows

| Topic | Example Query |
|---|---|
| Greetings | "Hello", "Hi there" |
| Machine Learning | "What is ML?" |
| Artificial Intelligence | "What is AI?" |
| Deep Learning | "Explain neural networks" |
| Python | "Tell me about Python" |
| Data Science | "What is Data Science?" |
| NLP | "What is NLP?" |
| Flask | "What is Flask?" |
| Chatbot identity | "Who are you?" |
| Farewells | "Bye", "Goodbye" |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Logic | Custom NLP (pattern matching + scoring) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Data | JSON knowledge base |

---

## 📸 Sample Output

```
Welcome to AI Chatbot!

User: Hello
Bot:  Hi! How can I help you today?

User: What is Machine Learning?
Bot:  Machine Learning is a branch of AI that allows systems to learn
      from data and improve over time without being explicitly programmed.

User: Bye
Bot:  Goodbye! Have a great day.
```

---

*Developed by Prashanth · Think Champ PVT LTD Internship*
=======
# AI Quiz Generator

## Project Description
This project is developed using Python fundamentals.
It asks random quiz questions from a text file and calculates the score.

## Concepts Used
- File Handling
- Loops
- Conditional Statements
- Random Module
- String Handling

## How It Works
1. Questions are stored in questions.txt
2. quiz.py reads all questions
3. Questions are shuffled randomly
4. User answers are checked
5. Final score is displayed and stored

## Future Improvements
- GUI using Tkinter
- Timer feature
- AI-generated questions
- Difficulty levels
- colored outputs

## How to Run
Run:

python quiz.py
>>>>>>> e993bfc7fca56c1619e57d891ecd8ad98bb44691
