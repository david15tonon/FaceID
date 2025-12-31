import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_line_chart(data, x_col, y_col, title="Line Chart"):
    """Create a line chart"""
    fig = px.line(data, x=x_col, y=y_col, title=title)
    return fig


def create_bar_chart(data, x_col, y_col, title="Bar Chart"):
    """Create a bar chart"""
    fig = px.bar(data, x=x_col, y=y_col, title=title)
    return fig


def create_pie_chart(data, values_col, names_col, title="Pie Chart"):
    """Create a pie chart"""
    fig = px.pie(data, values=values_col, names=names_col, title=title)
    return fig


def create_gauge_chart(value, title="Gauge"):
    """Create a gauge chart"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [None, 100]},
               'bar': {'color': "black"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgray"},
                   {'range': [50, 75], 'color': "gray"}],
               'threshold': {
                   'line': {'color': "red", 'width': 4},
                   'thickness': 0.75,
                   'value': 90}}))
    return fig
