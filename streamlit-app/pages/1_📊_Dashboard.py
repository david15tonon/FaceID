import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 Dashboard")
st.write("Real-time system metrics and analytics")

# Top Stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Verifications", "1,247", "+24")
with col2:
    st.metric("Success Rate", "98.7%", "+2.1%")
with col3:
    st.metric("Active Users", "156", "+12")
with col4:
    st.metric("Avg Response Time", "0.3s", "-0.1s")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Verification Trends")
    # Sample data
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    values = [100 + i * 5 + (i % 3) * 10 for i in range(len(dates))]
    df = pd.DataFrame({'Date': dates, 'Verifications': values})
    
    fig = px.line(df, x='Date', y='Verifications', title='Daily Verifications')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Success vs Failed")
    # Sample data
    labels = ['Successful', 'Failed']
    values = [1230, 17]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title='Verification Results')
    st.plotly_chart(fig, use_container_width=True)

# Recent Activity
st.markdown("---")
st.subheader("Recent Activity")

activity_data = {
    'Timestamp': ['2024-01-25 14:30', '2024-01-25 14:25', '2024-01-25 14:20'],
    'Event': ['Face Verified', 'Face Enrolled', 'Verification Failed'],
    'User': ['john.doe@example.com', 'jane.smith@example.com', 'Unknown'],
    'Status': ['✅ Success', '✅ Success', '❌ Failed']
}

st.dataframe(pd.DataFrame(activity_data), use_container_width=True)
