import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

st.set_page_config(
    page_title="FaceID Admin",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #000000;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666666;
        margin-bottom: 2rem;
    }
    .stat-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 2px solid #000000;
    }
    .stat-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #000000;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #666666;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# Main Page
st.markdown('<div class="main-header">🔐 FaceID System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Face Recognition Admin Dashboard</div>', unsafe_allow_html=True)

# Welcome message
st.info("👋 Welcome to FaceID! Select a page from the sidebar to get started.")

# Quick Stats
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">1,247</div>
        <div class="stat-label">Total Recognitions</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">98.7%</div>
        <div class="stat-label">Accuracy Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">156</div>
        <div class="stat-label">Active Users</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Features
st.subheader("Features")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📷 Face Enrollment")
    st.write("Register new faces in the system with live camera capture or image upload.")
    
    st.markdown("### 🔍 Face Verification")
    st.write("Verify identity against enrolled faces with high accuracy.")

with col2:
    st.markdown("### 📈 Analytics")
    st.write("View detailed analytics and insights on recognition performance.")
    
    st.markdown("### 📋 Logs")
    st.write("Access comprehensive audit trails and system logs.")

st.markdown("---")

# Getting Started
st.subheader("Getting Started")
st.write("""
1. **Enroll Faces**: Navigate to Face Enrollment to register new faces
2. **Verify Identity**: Use Face Verification to match against enrolled faces
3. **Monitor**: Check Dashboard for real-time statistics
4. **Review**: Examine Logs for detailed activity history
""")
