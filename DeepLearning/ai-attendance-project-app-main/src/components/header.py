import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div class="brand brand--home">
            <img src="{logo_url}" alt="AI Attendance System logo" />
            <h1>AI ATTENDANCE<br/>SYSTEM</h1>
        </div>
        """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div class="brand brand--dashboard">
            <img src="{logo_url}" alt="AI Attendance System logo" />
            <h2>AI ATTENDANCE<br/>SYSTEM</h2>
        </div>
        """, unsafe_allow_html=True)
