import streamlit as st


def display_face_grid(faces):
    """Display faces in a grid layout"""
    if not faces:
        st.info("No faces to display")
        return
    
    cols = st.columns(3)
    for idx, face in enumerate(faces):
        with cols[idx % 3]:
            st.image(face.get('image_url', ''), caption=face.get('name', 'Unknown'))
            st.caption(f"Enrolled: {face.get('enrolled_at', 'Unknown')}")


def display_face_card(face_data):
    """Display a single face card"""
    st.markdown(f"""
    <div style="border: 2px solid #000; padding: 1rem; margin: 0.5rem 0;">
        <h4>{face_data.get('name', 'Unknown')}</h4>
        <p><strong>Email:</strong> {face_data.get('email', 'N/A')}</p>
        <p><strong>Enrolled:</strong> {face_data.get('enrolled_at', 'N/A')}</p>
        <p><strong>Confidence:</strong> {face_data.get('confidence', 'N/A')}</p>
    </div>
    """, unsafe_allow_html=True)
