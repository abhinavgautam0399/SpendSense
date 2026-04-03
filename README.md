# 💸 SpendSense

A full-stack Expense Tracking and Analytics system built using FastAPI (Backend) and Streamlit (Frontend).

SpendSense helps users track daily expenses, manage records, and visualize spending patterns with an interactive and clean dashboard.

---

## 📌 What this project does

This project allows users to:

- Add expenses  
- Update expenses  
- View expense summary  
- Analyze expense breakdown by category  
- Visualize data using charts  

---

## 🚀 Tech Stack

### 🔹 Backend
- FastAPI  
- Uvicorn  
- Pydantic  

### 🔹 Frontend
- Streamlit  
- Pandas  
- Matplotlib  

### 🔹 Other
- Requests (API communication)

---

## 📁 Project Structure

```
project-expense-tracking-system/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   ├── logging_setup.py
│
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   ├── analytics_ui.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/project-expense-tracking-system.git
cd project-expense-tracking-system
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux
```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## 🔹 Start Backend (FastAPI)

From project root:

```
uvicorn backend.server:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

API Docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 Start Frontend (Streamlit)

Open a new terminal and run:

```
streamlit run frontend/app.py
```

Frontend will run on:

```
http://localhost:8501
```

---

# 📊 Features

- Add new expenses
- Update existing expenses
- Filter by date range
- View expense summary
- Category-wise percentage breakdown
- Bar chart visualization
- Clean UI using Streamlit

---

# 📌 Example Workflow

1. Start backend server
2. Start Streamlit frontend
3. Add expenses
4. Go to Analytics tab
5. Select date range
6. View breakdown and visualization

---

# 🧠 Learning Highlights

- REST API development using FastAPI
- API integration using Requests
- Data manipulation using Pandas
- Data visualization using Streamlit
- Debugging JSON and API responses
- Error handling and validation
- Project structuring for real-world applications

---

# 🔮 Future Improvements

- Add user authentication
- Add database (SQLite/PostgreSQL)
- Deploy on cloud (Render / Railway / AWS)
- Add CSV import feature
- Add dashboard improvements
- Add Docker support

---

# 📄 Requirements

Main dependencies:

```
fastapi
uvicorn
streamlit
pandas
matplotlib
pydantic
requests
```

---

# 👨‍💻 Author

Abhinav Gautam  
Aspiring Data Analyst / Data Scientist  

---

# ⭐ If you like this project

Give it a star ⭐ on GitHub