import streamlit as st

st.title("📱 ScrollStop Pro")
st.write("Mindful Browsing Simulator")

st.success("Go to Instagram Simulation from sidebar 👉")

# Button to open Instagram Simulation
if st.button("Open Simulations"):
    st.switch_page("pages/insta.py")