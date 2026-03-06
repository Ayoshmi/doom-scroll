import streamlit as st
import time

st.title("🧘 Mandatory Mindfulness Break")

st.error("Digital overload detected 🚨")
st.write("You must complete this breathing exercise.")

breath = st.empty()

# Breathing cycles
for _ in range(3):

    breath.info("🌬 Inhale...")
    time.sleep(3)

    breath.success("😌 Hold...")
    time.sleep(3)

    breath.warning("💨 Exhale...")
    time.sleep(3)

st.success("✅ Break Completed!")
st.write("You may now return to the app.")

# Optional return button
if st.button("Return Home"):
    st.switch_page("app.py")