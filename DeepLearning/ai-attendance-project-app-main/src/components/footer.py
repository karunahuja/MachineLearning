import streamlit as st


def footer_home():
    st.markdown("""
        <div class="app-footer app-footer--home">
        <span class="app-footer__mark" aria-hidden="true">AI</span>
        <p>Created by <strong>KARUN AHUJA</strong></p>
        </div>
        """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div class="app-footer">
        <span class="app-footer__mark" aria-hidden="true">AI</span>
        <p>Created by <strong>KARUN AHUJA</strong></p>
        </div>
        """, unsafe_allow_html=True)
