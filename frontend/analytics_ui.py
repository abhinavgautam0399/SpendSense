import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

import os
API_URL = os.getenv("API_URL", "http://localhost:8000")


def analytics_tab():
    st.markdown("## 📊 Expense Analytics")

    today = datetime.today()
    start = datetime(today.year, today.month, 1)

    start_date = st.date_input("Start Date", start)
    end_date = st.date_input("End Date", today)

    if st.button("Get Analytics"):
        st.session_state.show_analytics = True

    if "show_analytics" not in st.session_state:
        st.session_state.show_analytics = False

    if not st.session_state.show_analytics:
        return

    payload = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d")
    }

    res = requests.post(f"{API_URL}/analytics/", json=payload)

    if res.status_code != 200:
        st.error("Failed to fetch analytics data")
        return

    data = res.json()
    total = data["total"]
    breakdown = data["breakdown"]

    if not breakdown:
        st.warning("No expenses found for selected period")
        return

    df = pd.DataFrame([
        {"Category": k, "Total": v["total"], "Percentage": v["percentage"]}
        for k, v in breakdown.items()
    ])

    df = df.sort_values("Percentage", ascending=False)

    col1, col2 = st.columns(2)
    col1.metric("Total Spend", f"₹{total:,.0f}")
    col2.metric("Top Category", df.iloc[0]["Category"])

    if "budget" not in st.session_state:
        st.session_state.budget = 0.0

    if "budget_input" not in st.session_state:
        st.session_state.budget_input = st.session_state.budget

    st.subheader("Budget")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.number_input(
            "Monthly Budget",
            min_value=0.0,
            key="budget_input",
            label_visibility="collapsed"
        )

    with col2:
        if st.button("Update"):
            st.session_state.budget = st.session_state.budget_input

    budget = st.session_state.budget

    if budget > 0:
        usage = (total / budget) * 100
        remaining = budget - total

        col1, col2 = st.columns(2)
        col1.metric("Budget Used", f"{usage:.1f}%")

        if remaining >= 0:
            col2.metric("Saved", f"₹{remaining:,.0f}")
        else:
            col2.metric("Overspent", f"₹{abs(remaining):,.0f}")

        if usage >= 100:
            st.error("Budget exceeded")
        elif usage >= 80:
            st.warning("Budget almost used")
        else:
            st.success("Within budget")

    st.markdown("### Expense Distribution")

    colors = ['#A8E6CF', '#FFD3B6', '#FFAAA5', '#D5AAFF', '#A0C4FF']

    fig, ax = plt.subplots()

    ax.pie(
        df["Percentage"],
        labels=df["Category"],
        startangle=90,
        colors=colors,
        wedgeprops={
            'width': 0.38,
            'edgecolor': '#0E1117',
            'linewidth': 2
        },
        textprops={
            'color': '#EAEAEA',
            'fontsize': 13,
            'weight': 'bold'
        }
    )

    plt.text(
        0, 0,
        "Expense\nDistribution",
        ha='center',
        va='center',
        fontsize=15,
        color='#F5F5F5',
        weight='bold'
    )

    ax.set_facecolor('#0E1117')
    fig.patch.set_facecolor('#0E1117')

    st.pyplot(fig)

    st.bar_chart(df.set_index("Category")["Percentage"], use_container_width=True)

    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "expense_analytics.csv",
        "text/csv"
    )