import streamlit as st
import time

st.title("📊 Usage Result")

# ✅ Safety checks (avoid blank screen errors)
if "individual" not in st.session_state:
    st.session_state.individual = {}

if "total_time" not in st.session_state:
    st.session_state.total_time = 0

result = st.session_state.get("cumulative", "SAFE")

# -------------------------------
# Individual App Result
# -------------------------------
st.subheader("Individual App Intervention")

for app, status in st.session_state.individual.items():
    st.write(app, ":", status)

st.divider()

# -------------------------------
# Cumulative Result
# -------------------------------
st.subheader("Cumulative Intervention")

total_time = st.session_state.total_time
st.write("Total Time:", total_time, "minutes")

# -------------------------------
# STATUS CONDITIONS
# -------------------------------

if result == "SAFE":
    st.success("Healthy overall usage ✅")


elif result == "GENTLE":
    st.warning("Reduce total screen time 🙂")

    # ✅ Show cumulative usage message
    hours = total_time / 60
    st.info(
        f"⚠ You have already used {hours:.1f} hours today.\n"
        "Consider reflecting or taking a short mindful break."
    )



elif result == "AGGRESSIVE":
    st.error("Digital overload 🚨")
    st.write("Try breathing or focus activity")

    lock = st.empty()

    # Forced pause before redirect
    for i in range(5, 0, -1):   # change to 120 for real demo
        lock.warning(f"⛔ Redirecting to breathing exercise in {i} sec")
        time.sleep(1)

    # ✅ AUTOMATIC PAGE OPEN
    st.switch_page("pages/breathing.py")