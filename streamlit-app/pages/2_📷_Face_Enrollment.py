import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.set_page_config(page_title="Face Enrollment", page_icon="📷", layout="wide")

st.title("📷 Face Enrollment")
st.write("Register a new face in the system")

# Instructions
with st.expander("📋 Instructions", expanded=True):
    st.markdown("""
    1. **Position your face** within the camera frame
    2. **Ensure good lighting** on your face
    3. **Remove glasses** if possible
    4. **Look directly** at the camera
    5. **Stay still** when capturing
    """)

# Enrollment options
enrollment_method = st.radio("Choose enrollment method:", ["📸 Camera Capture", "📁 Upload Image"])

if enrollment_method == "📸 Camera Capture":
    st.info("🎥 Camera capture would be implemented here using streamlit-webrtc")
    
    # Placeholder for camera
    camera_placeholder = st.empty()
    camera_placeholder.image("https://via.placeholder.com/640x480/000000/FFFFFF?text=Camera+Feed", 
                             caption="Camera preview would appear here")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📸 Capture Face", type="primary", use_container_width=True):
            st.success("✅ Face captured successfully!")
            st.info("Face would be processed and enrolled here")

else:
    st.subheader("📁 Upload Face Image")
    
    uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # User details
        st.subheader("User Details")
        col1, col2 = st.columns(2)
        with col1:
            user_name = st.text_input("Full Name")
        with col2:
            user_email = st.text_input("Email")
        
        if st.button("✅ Enroll Face", type="primary", use_container_width=True):
            if user_name and user_email:
                st.success(f"✅ Face enrolled successfully for {user_name}!")
                st.balloons()
            else:
                st.error("❌ Please fill in all user details")

# Enrolled Faces
st.markdown("---")
st.subheader("Recently Enrolled")

enrolled_data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'Email': ['john@example.com', 'jane@example.com', 'mike@example.com'],
    'Enrolled At': ['2024-01-25 14:30', '2024-01-25 13:15', '2024-01-25 11:45'],
}

st.dataframe(enrolled_data, use_container_width=True)
