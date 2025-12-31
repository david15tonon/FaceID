# Stats cards component
import streamlit as st

def stats_card(title, value, delta=None):
    """Display a statistics card"""
    st.metric(label=title, value=value, delta=delta)
