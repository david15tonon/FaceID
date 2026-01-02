# Camera component
import streamlit as st

def camera_input():
    """Display camera input widget"""
    return st.camera_input("Take a picture")
