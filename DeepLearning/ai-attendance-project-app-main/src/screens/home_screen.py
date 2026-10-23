from pathlib import Path

import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    st.markdown(
        """
        <section class="home-hero" aria-labelledby="home-hero-title">
            <div class="home-hero__copy">
                <span class="home-eyebrow">SMARTER CLASSROOMS START HERE</span>
                <h2 id="home-hero-title">Attendance, made effortless.</h2>
                <p>Spend less time taking attendance and more time learning.
                Use AI-powered face and voice tools to make every class count.</p>
                <div class="home-hero__signature">
                    <span class="home-status-dot" aria-hidden="true"></span>
                    <span>Created by <strong>KARUN AHUJA</strong></span>
                </div>
            </div>
            <div class="home-hero__visual" aria-hidden="true">
                <div class="home-orbit home-orbit--outer"></div>
                <div class="home-orbit home-orbit--inner"></div>
                <div class="home-hero__ai">AI</div>
                <span class="home-orbit__spark home-orbit__spark--one"></span>
                <span class="home-orbit__spark home-orbit__spark--two"></span>
                <span class="home-orbit__spark home-orbit__spark--three"></span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="home-section-heading">
            <span class="home-eyebrow">YOUR CLASSROOM, CONNECTED</span>
            <h2>Choose your space</h2>
            <p>Sign in to get started with your classes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="home_portals"):
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown('<span class="portal-card__eyebrow">FOR LEARNERS</span>', unsafe_allow_html=True)
            st.header("I'm a student")
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
            st.markdown(
                '<p class="portal-card__description">Check in to class and keep track of your attendance.</p>',
                unsafe_allow_html=True,
            )
            if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
                st.session_state['login_type'] = 'student'
                st.rerun()

        with col2:
            st.markdown('<span class="portal-card__eyebrow">FOR EDUCATORS</span>', unsafe_allow_html=True)
            st.header("I'm a teacher")
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
            st.markdown(
                '<p class="portal-card__description">Manage subjects and review class attendance with ease.</p>',
                unsafe_allow_html=True,
            )
            if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
                st.session_state['login_type'] = 'teacher'
                st.rerun()

    st.markdown(
        """
        <section class="home-features" aria-label="AI Attendance System features">
            <article class="home-feature">
                <span class="home-feature__icon" aria-hidden="true">◎</span>
                <div><h3>AI-powered check-ins</h3>
                <p>Make taking attendance easier with face and voice tools.</p></div>
            </article>
            <article class="home-feature">
                <span class="home-feature__icon" aria-hidden="true">▦</span>
                <div><h3>Classroom, organized</h3>
                <p>Keep subjects, sections, and student enrollment together.</p></div>
            </article>
            <article class="home-feature">
                <span class="home-feature__icon" aria-hidden="true">↗</span>
                <div><h3>Records at a glance</h3>
                <p>Review attendance records whenever you need them.</p></div>
            </article>
        </section>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="experience_showcase"):
        st.markdown(
            """
            <div class="experience-heading">
                <span class="experience-heading__eyebrow">THE PERSON BEHIND THE PROJECT</span>
                <h2>Meet the creator</h2>
                <p>A people-first attendance system, shaped by experience across technology and industries.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        portrait_columns = st.columns([1, 1.2, 1])
        with portrait_columns[1]:
            with st.container(key="creator_portrait"):
                portrait_path = (
                    Path(__file__).resolve().parents[2] / "KarunAhuja.jpg"
                )
                st.image(
                    str(portrait_path),
                    width=180,
                    alt="Portrait of creator Karun Ahuja",
                )
                st.markdown(
                    '<p class="creator-portrait__name">Karun Ahuja</p>',
                    unsafe_allow_html=True,
                )

        st.markdown(
            """
            <div class="creator-bio">
                <span class="creator-bio__eyebrow">CREATOR &amp; BUILDER</span>
                <h3>Karun Ahuja</h3>
                <p class="creator-bio__role">Global Tech &amp; Business Strategist</p>
                <p>Bridging North American experience with Indian expertise.
                My work spans AI and automation across space, telecom, and
                healthcare—and informs the thoughtful, practical design of
                this attendance system.</p>
                <div class="creator-bio__tags">
                    <span>Artificial intelligence</span>
                    <span>Business analytics</span>
                    <span>Technology strategy</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        journey_image = (
            Path(__file__).resolve().parents[2]
            / "Gemini_Generated_Image_413hse413hse413h.jpeg"
        )
        st.image(
            str(journey_image),
            width="stretch",
            caption="Karun Ahuja — education and cross-industry experience highlights",
        )

        st.markdown(
            """
            <div class="experience-highlights" aria-label="Education and experience highlights">
                <article class="experience-highlight experience-highlight--analytics">
                    <span>01 / ANALYTICS</span>
                    <h3>Business analytics</h3>
                    <p>George Brown College<br/>Toronto, Canada</p>
                </article>
                <article class="experience-highlight experience-highlight--space">
                    <span>02 / SPACE &amp; AI</span>
                    <h3>Machine learning</h3>
                    <p>ISRO · Temporal satellite imagery</p>
                </article>
                <article class="experience-highlight experience-highlight--health">
                    <span>03 / HEALTHCARE</span>
                    <h3>Healthcare technology</h3>
                    <p>UHG · Fortune 5 experience</p>
                </article>
                <article class="experience-highlight experience-highlight--telecom">
                    <span>04 / TELECOM</span>
                    <h3>Automation &amp; networks</h3>
                    <p>Amdocs · Huawei · Ericsson · Nokia</p>
                </article>
            </div>
            """,
            unsafe_allow_html=True,
        )

    footer_home()