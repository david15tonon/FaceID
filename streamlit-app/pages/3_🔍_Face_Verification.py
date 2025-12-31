import streamlit as st
from PIL import Image

st.set_page_config(page_title="Face Verification", page_icon="🔍", layout="wide")

st.title("🔍 Face Verification")
st.write("Verify identity against enrolled faces")

# Verification method
verification_method = st.radio("Choose verification method:", ["📸 Camera Capture", "📁 Upload Image"])

if verification_method == "📸 Camera Capture":
    st.info("🎥 Camera capture would be implemented here using streamlit-webrtc")
    
    camera_placeholder = st.empty()
    camera_placeholder.image("https://via.placeholder.com/640x480/000000/FFFFFF?text=Camera+Feed", 
                             caption="Camera preview would appear here")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔍 Verify Identity", type="primary", use_container_width=True):
            # Simulate verification result
            st.success("✅ Match Found!")
            st.markdown("**Name:** John Doe")
            st.markdown("**Confidence:** 98.5%")
            st.markdown("**Email:** john@example.com")

else:
    st.subheader("📁 Upload Image for Verification")
    
    uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("Verification Result")
            
            if st.button("🔍 Verify", type="primary", use_container_width=True):
                with st.spinner("Verifying..."):
                    # Simulate verification
                    import time
                    time.sleep(1)
                    
                    # Show result
                    st.success("✅ Match Found!")
                    st.markdown("**Name:** John Doe")
                    st.markdown("**Confidence:** 98.5%")
                    st.markdown("**Email:** john@example.com")
                    st.markdown("**Last Verified:** Just now")

# Recent Verifications
st.markdown("---")
st.subheader("Recent Verifications")

verification_data = {
    'Timestamp': ['2024-01-25 14:30', '2024-01-25 14:25', '2024-01-25 14:20', '2024-01-25 14:15'],
    'Name': ['John Doe', 'Jane Smith', 'Unknown', 'Mike Johnson'],
    'Confidence': ['98.5%', '97.2%', 'No Match', '99.1%'],
    'Status': ['✅ Match', '✅ Match', '❌ No Match', '✅ Match']
}

st.dataframe(verification_data, use_container_width=True)
