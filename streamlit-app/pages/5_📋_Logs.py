import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logs", page_icon="📋", layout="wide")

st.title("📋 System Logs")
st.write("Comprehensive audit trail and activity logs")

# Filters
col1, col2, col3, col4 = st.columns(4)

with col1:
    event_filter = st.selectbox("Event Type:", ["All", "Verification", "Enrollment", "Failed"])
with col2:
    status_filter = st.selectbox("Status:", ["All", "Success", "Failed"])
with col3:
    date_from = st.date_input("From Date:")
with col4:
    date_to = st.date_input("To Date:")

# Search
search_query = st.text_input("🔍 Search logs...", placeholder="Search by user, IP, or event")

# Logs Table
st.subheader("Activity Logs")

log_data = {
    'Timestamp': ['2024-01-25 14:30:22', '2024-01-25 14:25:15', '2024-01-25 14:20:45', 
                  '2024-01-25 14:15:30', '2024-01-25 14:10:12', '2024-01-25 14:05:55',
                  '2024-01-25 14:00:33', '2024-01-25 13:55:18'],
    'Event': ['Face Verification', 'Face Enrollment', 'Face Verification', 
              'Face Verification', 'Face Verification', 'Face Enrollment',
              'Face Verification', 'Face Verification'],
    'User': ['john@example.com', 'jane@example.com', 'mike@example.com',
             'Unknown', 'sarah@example.com', 'alex@example.com',
             'john@example.com', 'jane@example.com'],
    'IP Address': ['192.168.1.100', '192.168.1.101', '192.168.1.102',
                   '192.168.1.103', '192.168.1.104', '192.168.1.105',
                   '192.168.1.100', '192.168.1.101'],
    'Status': ['✅ Success', '✅ Success', '✅ Success',
               '❌ Failed', '✅ Success', '✅ Success',
               '✅ Success', '✅ Success'],
    'Confidence': ['98.5%', '-', '97.2%', 'N/A', '99.1%', '-', '98.8%', '96.5%']
}

df = pd.DataFrame(log_data)
st.dataframe(df, use_container_width=True, height=400)

# Pagination
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.write("Showing 1-8 of 1,247 logs")

col1, col2, col3 = st.columns([2, 1, 1])
with col2:
    st.button("⬅️ Previous", use_container_width=True)
with col3:
    st.button("Next ➡️", use_container_width=True)

# Export
st.markdown("---")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("📥 Export to CSV", use_container_width=True):
        st.success("✅ Logs exported successfully!")
with col2:
    if st.button("📊 Generate Report", use_container_width=True):
        st.success("✅ Report generated successfully!")

# Log Statistics
st.markdown("---")
st.subheader("Log Statistics")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Logs", "1,247")
with col2:
    st.metric("Success Events", "1,230")
with col3:
    st.metric("Failed Events", "17")
with col4:
    st.metric("Unique Users", "156")
