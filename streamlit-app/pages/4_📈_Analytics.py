import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")

st.title("📈 Analytics")
st.write("Detailed insights and performance metrics")

# Time range selector
time_range = st.selectbox("Select Time Range:", ["Last 7 Days", "Last 30 Days", "Last 3 Months", "Last Year"])

# Key Metrics
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Verifications", "1,247", "+24 from last period")
with col2:
    st.metric("Success Rate", "98.7%", "+2.1%")
with col3:
    st.metric("Avg Confidence", "97.3%", "+1.5%")
with col4:
    st.metric("Failed Attempts", "17", "-3")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Verification Trends")
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    success = [90 + i * 3 + (i % 5) * 5 for i in range(len(dates))]
    failed = [5 + (i % 3) for i in range(len(dates))]
    
    df = pd.DataFrame({'Date': dates, 'Success': success, 'Failed': failed})
    fig = px.line(df, x='Date', y=['Success', 'Failed'], title='Daily Verification Trends')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Hourly Distribution")
    hours = list(range(24))
    verifications = [10, 8, 5, 3, 2, 5, 15, 30, 45, 60, 55, 50, 48, 52, 58, 62, 65, 68, 50, 35, 25, 20, 15, 12]
    
    df = pd.DataFrame({'Hour': hours, 'Verifications': verifications})
    fig = px.bar(df, x='Hour', y='Verifications', title='Verifications by Hour')
    st.plotly_chart(fig, use_container_width=True)

# Performance Metrics
st.markdown("---")
st.subheader("Performance Metrics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Response Time Distribution")
    response_times = pd.DataFrame({
        'Range': ['< 0.1s', '0.1-0.3s', '0.3-0.5s', '> 0.5s'],
        'Count': [450, 650, 130, 17]
    })
    fig = px.pie(response_times, values='Count', names='Range', title='Response Time Distribution')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Confidence Score Distribution")
    scores = pd.DataFrame({
        'Range': ['90-95%', '95-98%', '98-100%'],
        'Count': [230, 580, 437]
    })
    fig = px.bar(scores, x='Range', y='Count', title='Confidence Scores')
    st.plotly_chart(fig, use_container_width=True)

# Top Users
st.markdown("---")
st.subheader("Most Active Users")

user_data = {
    'User': ['john@example.com', 'jane@example.com', 'mike@example.com', 'sarah@example.com'],
    'Verifications': [247, 189, 156, 143],
    'Success Rate': ['99.2%', '98.4%', '97.8%', '99.0%']
}

st.dataframe(user_data, use_container_width=True)
