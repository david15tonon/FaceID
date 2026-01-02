# Charts component
import streamlit as st
import pandas as pd

def line_chart(data):
    """Display a line chart"""
    st.line_chart(data)

def bar_chart(data):
    """Display a bar chart"""
    st.bar_chart(data)
