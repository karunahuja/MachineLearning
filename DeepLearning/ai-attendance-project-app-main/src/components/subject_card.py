import streamlit as st
from html import escape


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="subject-card">
            <h3>{escape(str(name))}</h3>
            <p class="subject-card__details">
                Code <span class="subject-card__code">{escape(str(code))}</span>
                <span class="subject-card__separator">/</span>
                Section {escape(str(section))}
            </p>
        """

    if stats:
        html += """
        <div class="subject-card__stats">
        """
        for icon, label, value in stats:
            html += (
                '<div class="subject-card__stat">'
                f'<span>{escape(str(icon))}</span> '
                f'<b>{escape(str(value))}</b> '
                f'{escape(str(label))}'
                '</div>'
            )

        html += "</div>"

    st.markdown(f"{html}</div>", unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
