import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Travel Planner & Budget Estimator",
    page_icon="✈️",
    layout="centered"
)

# Title
st.title("✈️ Travel Planner & Budget Estimator")
st.write("Plan your trip and estimate your travel budget easily!")

st.divider()

# User Details
st.header("👤 Traveller Details")

name = st.text_input("Enter your name")

# Destination
destinations = ["Manali", "Goa", "Jaipur", "Kashmir"]
destination = st.selectbox(
    "📍 Choose your destination",
    destinations
)

# Trip Duration
days = st.number_input(
    "📅 Number of days",
    min_value=1,
    max_value=365,
    value=3,
    step=1
)

# Total Budget
budget = st.number_input(
    "💰 Total Budget (₹)",
    min_value=1000.0,
    value=10000.0,
    step=500.0
)

# Transport
transport = st.selectbox(
    "🚆 Choose Transport",
    ["Bus", "Train", "Flight"]
)

st.divider()

# Calculate Button
if st.button("🧮 Calculate My Trip", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter your name.")
    else:

        # Budget Distribution using NumPy
        categories = np.array(
            ["Hotel", "Food", "Transport", "Shopping"]
        )

        percentages = np.array(
            [40, 20, 25, 15]
        )

        amounts = (budget * percentages) / 100

        hotel = amounts[0]
        food = amounts[1]
        travel = amounts[2]
        shopping = amounts[3]

        # Daily Budget
        daily_budget = budget / days

        # Budget Level
        if budget < 10000:
            status = "Low Budget Trip"
        elif budget <= 30000:
            status = "Medium Budget Trip"
        else:
            status = "Luxury Budget Trip"

        # Pandas DataFrame
        df = pd.DataFrame({
            "Category": categories,
            "Percentage (%)": percentages,
            "Amount (₹)": amounts
        })

        # Remaining Budget
        remaining = budget - np.sum(amounts)

        # Travel Summary
        st.success("Trip plan calculated successfully! 🎉")

        st.header("📋 Travel Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Traveller Name:**", name)
            st.write("**Destination:**", destination)
            st.write("**Transport:**", transport)

        with col2:
            st.write("**Trip Duration:**", f"{days} Days")
            st.write("**Total Budget:**", f"₹{budget:,.2f}")
            st.write("**Budget Status:**", status)

        st.subheader("💰 Budget Distribution")

        # Display Pandas table
        display_df = df.copy()
        display_df["Amount (₹)"] = display_df["Amount (₹)"].round(2)

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        # Budget information
        st.subheader("📊 Budget Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Daily Budget",
                f"₹{daily_budget:,.2f}"
            )

        with col2:
            st.metric(
                "Remaining Budget",
                f"₹{remaining:,.2f}"
            )

        # Travel Suggestions
        st.subheader("💡 Travel Suggestions")

        if budget < 10000:
            st.write("• Stay in budget hotels.")
            st.write("• Use public transport.")
            st.write("• Limit shopping.")

        elif budget <= 30000:
            st.write("• Choose comfortable hotels.")
            st.write("• Enjoy sightseeing.")
            st.write("• Keep some emergency money.")

        else:
            st.write("• Enjoy luxury hotels.")
            st.write("• Book premium transport.")
            st.write("• Explore premium activities.")

        # Pie Chart
        st.subheader("🥧 Travel Budget Distribution")

        fig, ax = plt.subplots(figsize=(7, 7))

        ax.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Travel Budget Distribution")

        st.pyplot(fig)

        st.divider()

        st.write(
            "✨ Thank you for using Travel Planner & Budget Estimator!"
        )