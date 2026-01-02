import streamlit as st


def stat_card(title, value, delta=None, delta_color="normal"):
    """Display a statistics card"""
    st.metric(label=title, value=value, delta=delta, delta_color=delta_color)


def info_card(title, content, icon="ℹ️"):
    """Display an info card"""
    st.markdown(f"""
    <div style="border: 2px solid #000; padding: 1rem; margin: 0.5rem 0; background: #f8f9fa;">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def action_card(title, description, button_text, on_click=None):
    """Display an action card"""
    st.markdown(f"""
    <div style="border: 2px solid #000; padding: 1rem; margin: 0.5rem 0;">
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(button_text, key=f"btn_{title}"):
        if on_click:
            on_click()
