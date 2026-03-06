import streamlit as st
from utils.intervention_engine import individual_check, cumulative_check

st.title("📱 App Usage Simulation")

instagram = st.slider("Instagram",0,300)
netflix = st.slider("Netflix",0,300)
games = st.slider("Games",0,300)

open_count = st.slider("App Opens",0,20)

total_time = instagram + netflix + games

if st.button("Check Usage"):

    # ✅ Individual results
    st.session_state.individual = {
        "Instagram": individual_check(instagram),
        "Netflix": individual_check(netflix),
        "Games": individual_check(games)
    }

    # ✅ Cumulative result
    st.session_state.cumulative = cumulative_check(
        total_time, open_count
    )

    st.session_state.total_time = total_time

    st.switch_page("pages/result.py")