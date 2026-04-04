import streamlit as st
from datetime import datetime
import requests

import os
API_URL = os.getenv("API_URL", "http://localhost:8000")


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1))

    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):

        # Headers
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Amount")

        with col2:
            st.subheader("Category")

        with col3:
            st.subheader("Notes")

        expenses = []

        #LOOP
        for i in range(5):


            if i < len(existing_expenses):
                amount = existing_expenses[i].get("amount", 0.0)
                category = existing_expenses[i].get("category", "Shopping")
                notes = existing_expenses[i].get("notes", "")
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)


            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{selected_date}_{i}",
                    label_visibility="collapsed"
                )


            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category) if category in categories else 0,
                    key=f"category_{selected_date}_{i}",
                    label_visibility="collapsed"
                )


            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })


        submit_button = st.form_submit_button("Save Expenses")

        if submit_button:


            invalid_entries = [exp for exp in expenses if exp["amount"] <= 0]

            if len(invalid_entries) > 0:
                st.error("All amounts must be greater than 0 ")
                st.stop()


            response = requests.post(
                f"{API_URL}/expenses/{selected_date}",
                json=expenses
            )

            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")