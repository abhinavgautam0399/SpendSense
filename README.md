# 💸 SpendSense

A full-stack Expense Tracking and Analytics system built using FastAPI for backend services and Streamlit for an interactive frontend interface..

SpendSense helps users track daily expenses, manage records, and visualize spending patterns with an interactive and clean dashboard.

---

## 🌍 Deployment Architecture

- **Frontend:** Streamlit Cloud  
- **Backend:** FastAPI (Render)  
- **Database:** MySQL (Railway)  

---

## 🚀 What this project does

This project enables users to:

- Add and update daily expenses
- Filter expenses by custom date ranges
- View summarized expense insights
- Analyze category-wise spending distribution
- Visualize data using interactive charts
- Export expense data as CSV  

---

## 🧰 Tech Stack

### 🔹 Backend
- FastAPI
- Uvicorn
- Pydantic

### 🔹 Frontend
- Streamlit
- Pandas
- Matplotlib

### 🔹 Database
- MySQL (Railway)

### 🔹 Deployment
- Streamlit Cloud (Frontend)
- Render (Backend)
- Railway (Database)

### 🔹 Other
- Requests (API communication)
---

## 📁 Project Structure

```
Spensense/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   └── logging_setup.py
│
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   └── analytics_ui.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 📥 Clone the Repository

```bash
git clone https://github.com/abhinavgautam0399/SpendSense.git
cd SpendSense
```

---

### 🧪 Create Virtual Environment (Recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 🌐 Live Application

🔗 **Frontend (Streamlit App)**  
https://spendsense0399.streamlit.app  

🔗 **Backend API (Render)**  
https://spendsense-backend-m0ze.onrender.com  

🔗 **API Documentation**  
https://spendsense-backend-m0ze.onrender.com/docs  

---

### 💻 Run Locally (Optional)

#### Start Backend
```bash
uvicorn backend.server:app --reload
```

#### Start Frontend
```bash
streamlit run frontend/app.py
```

Frontend will run on:
```
http://localhost:8501
```

---

## ✨ Features

- Add new expenses  
- Update existing expenses  
- Filter by date range  
- View expense summary  
- Category-wise percentage breakdown  
- Bar chart visualization  
- Export expenses as CSV  
- Clean UI using Streamlit 

---

## 🚀 Example Workflow

1. Open the live application (Streamlit frontend)
2. Add daily expense entries
3. Data is sent to backend API (Render)
4. Backend processes and stores data in Railway MySQL database
5. Navigate to Analytics tab
6. View insights and visualizations
7. Export data as CSV if needed
---

## 📚 Learning Highlights

- Built RESTful APIs using FastAPI
- Integrated frontend with backend APIs using HTTP requests
- Managed cloud-hosted database using Railway (MySQL)
- Deployed backend services on Render
- Deployed frontend on Streamlit Cloud
- Performed data manipulation using Pandas
- Created visualizations using Matplotlib
- Handled API errors and structured responses
- Designed a modular full-stack project architecture
---

## 🚀 Future Improvements

- Add user authentication (login/signup)
- Migrate to PostgreSQL for better scalability
- Add advanced analytics dashboard
- Implement Docker for containerization
- Add caching for performance optimization
---

## 📦 Requirements

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
## 👤 Author

Abhinav Gautam  
Aspiring Data Analyst / Data Scientist  

📧 Email: gautamabhinav456@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/abhinav-gautam-6a922b22a
## ⭐ If you like this project

Give it a ⭐ on GitHub
