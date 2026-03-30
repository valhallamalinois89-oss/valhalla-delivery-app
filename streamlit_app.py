import streamlit as st

st.set_page_config(page_title="Valhalla Delivery", page_icon="🐾")
st.title("⚔️ Valhalla Malinois Delivery Quote")

# --- INPUTS ---
st.header("1. Vehicle & Fuel")
mpg = st.number_input("Enter Vehicle MPG", min_value=1.0, value=15.0, step=0.1)
gas_price = st.number_input("Current Gas Price ($/gal)", value=3.50, step=0.01)

st.header("2. Route")
miles = st.number_input("One-Way Miles", min_value=0.0, value=0.0)
round_trip = st.toggle("Calculate Round Trip", value=True)

# --- MATH ---
multiplier = 2 if round_trip else 1
total_miles = miles * multiplier
total_cost = (total_miles / mpg) * gas_price

# --- RESULTS ---
st.divider()
st.metric("Estimated Fuel Cost", f"${total_cost:.2f}")

st.info("Copy this for the client:")
st.code(f"Valhalla Malinois Delivery\nTotal Fuel Quote: ${total_cost:.2f}")
