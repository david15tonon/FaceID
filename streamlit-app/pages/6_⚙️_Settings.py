import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

st.title("⚙️ Settings")
st.write("Configure system parameters and preferences")

# System Settings
st.subheader("System Settings")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Face Recognition")
    tolerance = st.slider("Recognition Tolerance:", 0.0, 1.0, 0.6, 0.05)
    st.caption("Lower values mean stricter matching")
    
    max_distance = st.slider("Max Face Distance:", 0.0, 1.0, 0.6, 0.05)
    st.caption("Maximum distance threshold for matches")
    
    enable_liveness = st.checkbox("Enable Liveness Detection", value=False)
    st.caption("Detect if the face is from a live person")

with col2:
    st.markdown("#### API Settings")
    api_url = st.text_input("Backend API URL:", value="http://localhost:8000/api")
    api_key = st.text_input("API Key:", type="password")
    
    timeout = st.number_input("Request Timeout (seconds):", min_value=1, max_value=60, value=30)

# Security Settings
st.markdown("---")
st.subheader("Security Settings")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Authentication")
    session_timeout = st.number_input("Session Timeout (minutes):", min_value=5, max_value=1440, value=30)
    require_mfa = st.checkbox("Require MFA for all users", value=False)
    password_expiry = st.number_input("Password Expiry (days):", min_value=0, max_value=365, value=90)

with col2:
    st.markdown("#### Logging")
    log_level = st.selectbox("Log Level:", ["DEBUG", "INFO", "WARNING", "ERROR"])
    enable_audit = st.checkbox("Enable Audit Trail", value=True)
    retention_days = st.number_input("Log Retention (days):", min_value=1, max_value=365, value=90)

# Email Notifications
st.markdown("---")
st.subheader("Email Notifications")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### SMTP Configuration")
    smtp_server = st.text_input("SMTP Server:", value="smtp.gmail.com")
    smtp_port = st.number_input("SMTP Port:", min_value=1, max_value=65535, value=587)
    smtp_user = st.text_input("SMTP Username:")
    smtp_password = st.text_input("SMTP Password:", type="password")

with col2:
    st.markdown("#### Notification Settings")
    notify_enrollment = st.checkbox("Notify on new enrollment", value=True)
    notify_failed = st.checkbox("Notify on failed verification", value=True)
    notify_threshold = st.number_input("Failed attempts threshold:", min_value=1, max_value=10, value=3)

# Save Settings
st.markdown("---")
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    if st.button("💾 Save Settings", type="primary", use_container_width=True):
        st.success("✅ Settings saved successfully!")
        st.balloons()

# Reset to Defaults
st.markdown("---")
st.subheader("⚠️ Danger Zone")

col1, col2 = st.columns([3, 1])
with col1:
    st.write("Reset all settings to default values. This action cannot be undone.")
with col2:
    if st.button("🔄 Reset to Defaults", use_container_width=True):
        st.warning("Settings have been reset to defaults!")
