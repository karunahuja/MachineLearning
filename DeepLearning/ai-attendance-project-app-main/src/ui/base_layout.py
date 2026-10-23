import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp,
            [data-testid="stAppViewContainer"] {
                background-color: #131b45 !important;
                background-image:
                    linear-gradient(115deg, rgba(10, 16, 44, .9), rgba(19, 29, 75, .76) 52%, rgba(13, 32, 58, .83)),
                    url("https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=2400&q=85"),
                    linear-gradient(135deg, #131b45 0%, #202d68 48%, #263978 100%) !important;
                background-position: center, center 48%, center !important;
                background-size: cover, cover, cover !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }

            [data-testid="stMain"],
            [data-testid="stMainBlockContainer"] {
                background: transparent !important;
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                min-height: 340px;
                padding: clamp(1.35rem, 4vw, 2.2rem) !important;
                border: 1px solid rgba(255, 255, 255, .92);
                border-radius: 26px !important;
                background: #fff !important;
                box-shadow: 0 22px 60px rgba(9, 15, 55, .28);
                transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover {
                transform: translateY(-5px);
                border-color: #9de7dc;
                box-shadow: 0 30px 72px rgba(9, 15, 55, .36);
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:first-child {
                border-top: 5px solid #12a99a;
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:last-child {
                border-top: 5px solid #6575ef;
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] h1,
            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] h2,
            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] h3 {
                color: #182044;
                text-align: center;
            }

            .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] [data-testid="stImage"] {
                display: flex;
                justify-content: center;
            }

            .home-eyebrow,
            .portal-card__eyebrow {
                color: #26334d;
                font-size: .72rem;
                font-weight: 800;
                letter-spacing: .14em;
            }

            .home-hero {
                position: relative;
                display: grid;
                grid-template-columns: minmax(0, 1.35fr) minmax(210px, .65fr);
                align-items: center;
                gap: 2rem;
                min-height: 310px;
                margin: .5rem 0 3rem;
                padding: clamp(1.5rem, 5vw, 3.5rem);
                overflow: hidden;
                border: 1px solid rgba(255, 255, 255, .92);
                border-radius: 30px;
                background:
                    radial-gradient(ellipse at 88% 12%, rgba(76, 208, 190, .24), transparent 38%),
                    radial-gradient(ellipse at 8% 100%, rgba(141, 125, 255, .18), transparent 48%),
                    linear-gradient(125deg, #ffffff 0%, #f4f7ff 54%, #effbf9 100%);
                box-shadow: 0 24px 70px rgba(4, 10, 37, .28);
                animation: home-rise-in .65s ease-out both;
            }

            .home-hero__copy { position: relative; z-index: 1; }

            .home-hero__copy .home-eyebrow {
                display: inline-flex;
                align-items: center;
                gap: .55rem;
                margin-bottom: 1.1rem;
                color: #26334d;
            }

            .home-hero__copy .home-eyebrow::before {
                width: 22px;
                height: 2px;
                background: #079b88;
                content: "";
            }

            .home-hero h2 {
                max-width: 650px;
                margin: 0 0 .9rem !important;
                color: #111827 !important;
                font-size: clamp(2.25rem, 5vw, 4rem) !important;
                line-height: 1.02 !important;
                letter-spacing: -.055em;
            }

            .home-hero__copy > p {
                max-width: 580px;
                margin: 0;
                color: #344054 !important;
                font-size: clamp(1rem, 1.5vw, 1.13rem);
                line-height: 1.75;
            }

            .home-hero__signature {
                display: inline-flex;
                align-items: center;
                gap: .6rem;
                margin-top: 1.65rem;
                color: #344054;
                font-size: .88rem;
            }

            .home-hero__signature strong {
                color: #111827;
                letter-spacing: .06em;
            }

            .home-status-dot {
                width: 9px;
                height: 9px;
                border-radius: 50%;
                background: #66dfcb;
                box-shadow: 0 0 0 5px rgba(102, 223, 203, .14);
            }

            .home-hero__visual {
                position: relative;
                display: grid;
                width: min(100%, 250px);
                aspect-ratio: 1;
                place-items: center;
                justify-self: center;
            }

            .home-orbit {
                position: absolute;
                border: 1px solid rgba(220, 229, 255, .3);
                border-radius: 50%;
            }

            .home-orbit--outer {
                inset: 4%;
                animation: home-orbit 28s linear infinite;
            }

            .home-orbit--inner {
                inset: 19%;
                border-color: rgba(122, 221, 211, .44);
                box-shadow: 0 0 50px rgba(74, 198, 189, .12), inset 0 0 50px rgba(74, 198, 189, .08);
                animation: home-orbit 20s linear infinite reverse;
            }

            .home-hero__ai {
                display: grid;
                width: 42%;
                aspect-ratio: 1;
                place-items: center;
                border: 1px solid rgba(255, 255, 255, .52);
                border-radius: 30%;
                background: linear-gradient(145deg, rgba(255, 255, 255, .36), rgba(113, 226, 213, .2));
                box-shadow: 0 18px 50px rgba(4, 10, 37, .22), inset 0 1px rgba(255, 255, 255, .35);
                color: #fff;
                font-size: clamp(2.5rem, 5vw, 3.6rem);
                font-weight: 800;
                letter-spacing: -.08em;
                backdrop-filter: blur(8px);
            }

            .home-orbit__spark {
                position: absolute;
                width: 11px;
                height: 11px;
                border: 2px solid #d9e5ff;
                border-radius: 50%;
                background: #68dbcc;
                box-shadow: 0 0 18px rgba(104, 219, 204, .8);
            }

            .home-orbit__spark--one { top: 13%; right: 19%; }
            .home-orbit__spark--two { bottom: 17%; left: 13%; width: 8px; height: 8px; }
            .home-orbit__spark--three { right: 8%; bottom: 34%; width: 7px; height: 7px; }

            .home-section-heading {
                margin: 0 auto 1.35rem;
                padding: 1.25rem 1.5rem;
                border: 1px solid rgba(255, 255, 255, .88);
                border-radius: 20px;
                background: linear-gradient(110deg, #fff 0%, #f2f5ff 55%, #effbf9 100%);
                box-shadow: 0 14px 38px rgba(4, 10, 37, .2);
                text-align: center;
            }

            .home-section-heading .home-eyebrow {
                color: #344054;
            }

            .home-section-heading h2 {
                margin: .45rem 0 .35rem !important;
                color: #111827 !important;
                font-size: clamp(1.8rem, 3vw, 2.35rem) !important;
            }

            .home-section-heading p {
                margin: 0;
                color: #344054 !important;
            }

            .portal-card__eyebrow {
                display: block;
                margin-bottom: .6rem;
                color: #4052b8;
                text-align: center;
            }

            .st-key-home_portals .portal-card__description {
                min-height: 3.1em;
                margin: .2rem 0 1rem;
                color: #53617a !important;
                line-height: 1.6;
                text-align: center;
            }

            .st-key-home_portals div[data-testid="stButton"] > button {
                min-height: 3.1rem;
                border-radius: 15px !important;
            }

            .st-key-home_portals div[data-testid="stButton"] > button[kind="primary"] {
                background: linear-gradient(135deg, #4055d0, #3445b4) !important;
                box-shadow: 0 8px 18px rgba(55, 73, 185, .25);
            }

            .st-key-home_portals div[data-testid="stButton"] > button[kind="primary"]:hover {
                background: linear-gradient(135deg, #3448bc, #29399e) !important;
            }

            .home-features {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 1rem;
                margin: 2rem 0 1rem;
            }

            .home-feature {
                display: flex;
                align-items: flex-start;
                gap: .9rem;
                padding: 1.2rem;
                border: 1px solid rgba(255, 255, 255, .9);
                border-radius: 18px;
                background: #fff;
                box-shadow: 0 12px 30px rgba(7, 15, 50, .18);
                transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
            }

            .home-feature:hover {
                transform: translateY(-3px);
                border-color: #a8e9df;
                box-shadow: 0 18px 38px rgba(7, 15, 50, .24);
            }

            .home-feature__icon {
                display: grid;
                flex: 0 0 42px;
                width: 42px;
                height: 42px;
                place-items: center;
                border: 1px solid #dce2ff;
                border-radius: 13px;
                background: #edf0ff;
                color: #3549bd;
                font-size: 1.45rem;
                font-weight: 700;
            }

            .home-feature:nth-child(2) .home-feature__icon {
                border-color: #c8eee6;
                background: #e7f8f3;
                color: #08766c;
            }

            .home-feature:nth-child(3) .home-feature__icon {
                border-color: #f3d9b0;
                background: #fff5e5;
                color: #975600;
            }

            .home-feature h3 {
                margin: .1rem 0 .35rem !important;
                color: #17213d !important;
                font-size: 1rem !important;
                letter-spacing: -.02em;
            }

            .home-feature p {
                margin: 0;
                color: #4d5b73 !important;
                font-size: .88rem;
                line-height: 1.55;
            }

            .st-key-experience_showcase {
                margin: 2.5rem 0 1.5rem;
                padding: clamp(1rem, 3vw, 2rem);
                overflow: hidden;
                border: 1px solid rgba(255, 255, 255, .92);
                border-radius: 26px;
                background: linear-gradient(135deg, #fff 0%, #f5f7ff 58%, #effaf8 100%);
                box-shadow: 0 22px 58px rgba(7, 15, 50, .25);
            }

            .experience-heading {
                max-width: 760px;
                margin: 0 auto 1.25rem;
                text-align: center;
            }

            .experience-heading__eyebrow {
                color: #3e50c8;
                font-size: .72rem;
                font-weight: 800;
                letter-spacing: .14em;
            }

            .experience-heading h2 {
                margin: .5rem 0 !important;
                color: #17213d !important;
                font-size: clamp(1.65rem, 3.6vw, 2.5rem) !important;
                line-height: 1.12 !important;
            }

            .experience-heading p {
                margin: 0 auto;
                color: #4d5b73 !important;
                font-size: .98rem;
                line-height: 1.65;
            }

            .st-key-experience_showcase .st-key-creator_portrait [data-testid="stImage"] {
                display: flex;
                width: 100%;
                margin: 0 auto;
                justify-content: center;
                overflow: visible !important;
                border: 0;
                border-radius: 0;
                background: transparent !important;
                box-shadow: none;
            }

            .st-key-experience_showcase .st-key-creator_portrait {
                width: 100% !important;
                align-items: center !important;
            }

            .st-key-experience_showcase .st-key-creator_portrait [data-testid="stImage"] img {
                display: block;
                width: 180px !important;
                height: 180px !important;
                aspect-ratio: 1;
                box-sizing: border-box;
                border: 3px solid #fff;
                border-radius: 50% !important;
                object-fit: cover;
                object-position: center 36%;
                box-shadow: 0 12px 30px rgba(35, 48, 94, .2);
            }

            .creator-portrait__name {
                margin: .7rem 0 0;
                color: #17213d !important;
                font-size: 1.05rem;
                font-weight: 800;
                letter-spacing: -.015em;
                text-align: center;
            }

            .st-key-experience_showcase .st-key-creator_portrait [data-testid="stImage"] figcaption {
                position: absolute;
                width: 1px;
                height: 1px;
                padding: 0;
                overflow: hidden;
                clip: rect(0, 0, 0, 0);
                white-space: nowrap;
                clip-path: inset(50%);
            }

            .creator-bio {
                max-width: 820px;
                margin: 1rem auto 0;
                padding: clamp(1rem, 3vw, 1.65rem);
                border: 1px solid #dfe5f1;
                border-radius: 20px;
                background: rgba(255, 255, 255, .86);
                box-shadow: 0 10px 28px rgba(35, 48, 94, .07);
                text-align: center;
            }

            .creator-bio * { text-align: center; }

            .creator-bio__eyebrow {
                color: #3e50c8;
                font-size: .7rem;
                font-weight: 800;
                letter-spacing: .14em;
            }

            .creator-bio h3 {
                margin: .45rem 0 .15rem !important;
                color: #17213d !important;
                font-size: clamp(1.6rem, 3vw, 2.15rem) !important;
                letter-spacing: -.04em;
            }

            .creator-bio__role {
                margin: 0 0 .75rem;
                color: #4052b8 !important;
                font-size: 1rem;
                font-weight: 700;
            }

            .creator-bio > p:not(.creator-bio__role) {
                max-width: 620px;
                margin: 0 auto;
                color: #46546c !important;
                font-size: .94rem;
                line-height: 1.7;
            }

            .creator-bio__tags {
                display: flex;
                flex-wrap: wrap;
                gap: .5rem;
                margin-top: 1rem;
                justify-content: center;
            }

            .creator-bio__tags span {
                padding: .35rem .65rem;
                border: 1px solid #dce2f4;
                border-radius: 999px;
                background: #f3f5ff;
                color: #34458f;
                font-size: .76rem;
                font-weight: 700;
            }

            .st-key-experience_showcase [data-testid="stImage"] {
                margin: 1.25rem 0;
                padding: .45rem;
                overflow: hidden;
                border: 1px solid #dce3f0;
                border-radius: 18px;
                background: #f5f7ff;
                box-shadow: 0 12px 30px rgba(17, 28, 61, .18);
            }

            .st-key-experience_showcase [data-testid="stImage"] img {
                display: block;
                width: 100%;
                height: auto;
                border-radius: 12px;
            }

            .st-key-experience_showcase [data-testid="stImage"] figcaption {
                padding: .45rem .3rem .15rem;
                color: #4d5b73 !important;
                font-size: .82rem;
                text-align: center;
            }

            .experience-highlights {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: .8rem;
                margin-top: 1.1rem;
            }

            .experience-highlight {
                min-height: 145px;
                padding: 1rem;
                border: 1px solid #e1e6f0;
                border-top: 4px solid #5367dc;
                border-radius: 15px;
                background: #fff;
                box-shadow: 0 7px 20px rgba(25, 39, 78, .06);
                transition: transform .18s ease, box-shadow .18s ease;
            }

            .experience-highlight:hover {
                transform: translateY(-3px);
                box-shadow: 0 12px 26px rgba(25, 39, 78, .12);
            }

            .experience-highlight--space { border-top-color: #078f82; }
            .experience-highlight--health { border-top-color: #cc8a28; }
            .experience-highlight--telecom { border-top-color: #7353bf; }

            .experience-highlight span {
                color: #53617a;
                font-size: .65rem;
                font-weight: 800;
                letter-spacing: .08em;
            }

            .experience-highlight h3 {
                margin: .65rem 0 .4rem !important;
                color: #17213d !important;
                font-size: 1rem !important;
                letter-spacing: -.02em;
            }

            .experience-highlight p {
                margin: 0;
                color: #4d5b73 !important;
                font-size: .82rem;
                line-height: 1.5;
            }

            @media (max-width: 700px) {
                .stApp { background-attachment: scroll !important; }

                .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                    min-height: 0;
                    padding: 1.35rem !important;
                    border-radius: 22px !important;
                }

                .home-hero {
                    grid-template-columns: 1fr;
                    gap: .75rem;
                    min-height: 0;
                    margin-bottom: 2.25rem;
                    padding: 1.6rem;
                    border-radius: 24px;
                }

                .home-hero__visual {
                    width: min(58vw, 190px);
                    margin: .4rem auto 0;
                }

                .home-section-heading { margin-bottom: 1rem; }
                .home-features { grid-template-columns: 1fr; gap: .7rem; }
                .home-feature { padding: 1rem; }
                .st-key-experience_showcase {
                    margin-top: 1.75rem;
                    padding: 1rem;
                    border-radius: 20px;
                }

                .st-key-experience_showcase .st-key-creator_portrait [data-testid="stImage"] img {
                    width: 150px !important;
                    height: 150px !important;
                }

                .experience-highlights { grid-template-columns: repeat(2, minmax(0, 1fr)); }
                .experience-highlight { min-height: 0; padding: .85rem; }
            }

            @media (max-width: 420px) {
                .experience-highlights { grid-template-columns: 1fr; }
            }

            @media (prefers-reduced-motion: reduce) {
                .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"],
                .home-feature,
                .experience-highlight {
                    transition: none;
                }

                .st-key-home_portals div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover,
                .home-feature:hover,
                .experience-highlight:hover {
                    transform: none;
                }

                .home-hero,
                .home-orbit--outer,
                .home-orbit--inner {
                    animation: none;
                }
            }

            @keyframes home-rise-in {
                from { opacity: 0; transform: translateY(12px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @keyframes home-orbit {
                to { transform: rotate(360deg); }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(ellipse at 100%, rgba(81, 104, 255, .09), transparent 34%),
                    radial-gradient(ellipse at 0%, rgba(24, 184, 170, .045), transparent 30%),
                    linear-gradient(180deg, #fafbff 0%, #f3f5fb 100%) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            :root {
                color-scheme: light;
                --ink: #17213d;
                --muted: #53617a;
                --brand: #4f62e8;
                --brand-dark: #3e50c8;
                --accent: #078f82;
                --line: #e3e8f2;
                --surface: #ffffff;
                --background-color: #f5f7fc;
                --secondary-background-color: #ffffff;
                --text-color: #17213d;
                --secondary-text-color: #53617a;
                --border-color: #e3e8f2;
                --background: #f5f7fc;
                --shadow: 0 14px 38px rgba(35, 48, 94, .075);
                --primary-color: #3e50c8;
            }

            #MainMenu, footer, header { visibility: hidden; }

            .stApp,
            [data-testid="stAppViewContainer"],
            [data-testid="stMain"],
            [data-testid="stMainBlockContainer"],
            [data-testid="stDialog"] {
                color-scheme: light !important;
                color: var(--ink) !important;
            }

            [data-testid="stAppViewContainer"],
            [data-testid="stMain"],
            [data-testid="stMainBlockContainer"] {
                background-color: transparent !important;
            }

            html {
                scroll-behavior: smooth;
                font-size: 16px;
            }

            body, [class*="css"] {
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                color: var(--ink);
            }

            input[type="checkbox"], input[type="radio"], input[type="range"] {
                accent-color: var(--brand-dark);
            }

            .stApp, .stApp p, .stApp li, .stApp td, .stApp th,
            .stApp legend, .stApp [data-testid="stMarkdownContainer"] {
                color: var(--ink);
            }

            .stApp p, .stApp [data-testid="stCaptionContainer"],
            .stApp [data-testid="stHelp"], .stApp small {
                color: var(--muted);
            }

            .stApp {
                color: var(--ink) !important;
                background-color: #f5f7fc !important;
                -webkit-font-smoothing: antialiased;
            }

            .block-container {
                width: min(100% - 2rem, 1160px);
                max-width: 1160px;
                padding-top: clamp(1.25rem, 3vw, 2.25rem) !important;
                padding-bottom: clamp(2rem, 5vw, 3.5rem) !important;
            }

            h1, h2, h3, h4, h5, h6 {
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
                color: var(--ink);
                letter-spacing: -.035em;
            }

            h1 { font-size: clamp(2.15rem, 5vw, 3.35rem) !important; line-height: 1.08 !important; }
            h2 { font-size: clamp(1.65rem, 3vw, 2.2rem) !important; line-height: 1.15 !important; }
            h3 { font-size: 1.35rem !important; line-height: 1.25 !important; }
            label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] *,
            [data-testid="stCheckbox"] label, [data-testid="stRadio"] label,
            [data-testid="stToggle"] label {
                color: var(--ink) !important;
            }

            .brand {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: .8rem;
            }

            .brand img {
                height: 76px;
                width: auto;
                object-fit: contain;
            }

            .brand h1, .brand h2 {
                margin: 0 !important;
                color: var(--brand) !important;
                font-size: 2rem !important;
                line-height: .95 !important;
                letter-spacing: -.045em;
                font-weight: 800;
            }

            .brand--home {
                flex-direction: column;
                gap: .35rem;
                width: fit-content;
                margin: 1.5rem auto 2rem;
                padding: 1.15rem 2rem 1.3rem;
                border: 1px solid rgba(255, 255, 255, .9);
                border-radius: 24px;
                background: rgba(255, 255, 255, .97);
                box-shadow: 0 16px 42px rgba(4, 10, 37, .22);
            }

            .brand--home img { height: 92px; }
            .brand--home h1 {
                color: #111827 !important;
                text-align: center;
                font-size: clamp(2rem, 5.5vw, 3.6rem) !important;
                line-height: 1.02 !important;
            }

            .brand--dashboard { justify-content: flex-start; }
            .brand--dashboard h2 { font-size: clamp(1.05rem, 2vw, 1.65rem) !important; }

            .app-footer {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: .5rem;
                margin-top: 2rem;
                opacity: 1;
            }

            .app-footer p {
                margin: 0;
                color: var(--muted);
                font-size: .9rem;
                font-weight: 600;
            }

            .app-footer p strong { color: var(--ink); letter-spacing: .055em; }
            .app-footer__mark {
                display: grid;
                width: 27px;
                height: 27px;
                place-items: center;
                border: 1px solid rgba(79, 98, 232, .2);
                border-radius: 9px;
                background: #edf0ff;
                color: var(--brand-dark);
                font-size: .72rem;
                font-weight: 800;
            }

            .app-footer--home {
                width: fit-content;
                margin: 2rem auto 0;
                padding: .65rem 1rem;
                border: 1px solid rgba(255, 255, 255, .88);
                border-radius: 999px;
                background: rgba(255, 255, 255, .97);
                box-shadow: 0 10px 28px rgba(4, 10, 37, .2);
            }

            .app-footer--home p,
            .app-footer--home p strong { color: #111827; }

            .subject-card {
                position: relative;
                margin: .25rem 0 1rem;
                padding: clamp(1rem, 2.5vw, 1.4rem);
                overflow: hidden;
                border: 1px solid var(--line);
                border-left: 4px solid var(--brand);
                border-radius: 20px;
                background: #fff;
                box-shadow: 0 8px 24px rgba(35, 48, 94, .06);
                transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
            }

            .subject-card:hover {
                transform: translateY(-3px);
                border-left-color: var(--accent);
                box-shadow: 0 14px 32px rgba(35, 48, 94, .12);
            }

            .subject-card:focus-within {
                outline: 3px solid rgba(79, 98, 232, .22);
                outline-offset: 2px;
            }

            .subject-card h3 {
                margin: 0 !important;
                color: var(--ink);
                font-size: 1.35rem !important;
            }

            .subject-card__details {
                display: flex;
                align-items: center;
                flex-wrap: wrap;
                gap: .45rem;
                margin: .65rem 0 1rem;
                font-size: .9rem;
            }

            .subject-card__code {
                padding: .2rem .55rem;
                border: 1px solid #e2e7ff;
                border-radius: 7px;
                background: #f0f2ff;
                color: var(--brand-dark);
                font-weight: 700;
            }

            .subject-card__separator { color: #b7bfd0; }

            .subject-card__stats {
                display: flex;
                flex-wrap: wrap;
                gap: .55rem;
            }

            .subject-card__stat {
                display: inline-flex;
                align-items: center;
                gap: .3rem;
                padding: .45rem .7rem;
                border: 1px solid #e8ecf5;
                border-radius: 10px;
                background: #f8f9fd;
                color: #52607c;
                font-size: .85rem;
            }

            .subject-card__stat b { color: var(--ink); }

            [data-testid="stVerticalBlockBorderWrapper"] {
                border: 1px solid var(--line) !important;
                border-radius: 22px !important;
                background: var(--surface) !important;
                box-shadow: var(--shadow);
            }

            div[data-testid="stButton"] > button,
            div[data-testid="stFormSubmitButton"] > button,
            div[data-testid="stDownloadButton"] > button {
                min-height: 2.9rem;
                border: 1px solid transparent !important;
                border-radius: 13px !important;
                padding: .55rem 1.1rem !important;
                font-family: inherit !important;
                font-weight: 700 !important;
                letter-spacing: .005em;
                transition: transform .18s ease, box-shadow .18s ease, background-color .18s ease, border-color .18s ease !important;
            }

            div[data-testid="stButton"] > button[kind="primary"],
            div[data-testid="stFormSubmitButton"] > button[kind="primary"],
            div[data-testid="stDownloadButton"] > button {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
                background: linear-gradient(135deg, #4659d4, #3647b5) !important;
                box-shadow: 0 7px 16px rgba(83, 103, 245, .22);
            }

            div[data-testid="stButton"] > button[kind="secondary"] {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
                background: linear-gradient(135deg, #08796f, #05645b) !important;
                box-shadow: 0 7px 16px rgba(8, 143, 130, .2);
            }

            div[data-testid="stFormSubmitButton"] > button[kind="secondary"] {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
                background: linear-gradient(135deg, #08796f, #05645b) !important;
            }

            div[data-testid="stButton"] > button[kind="tertiary"] {
                color: #273450 !important;
                -webkit-text-fill-color: #273450 !important;
                background: #edf0f8 !important;
                border-color: #d8dfed !important;
            }

            div[data-testid="stFormSubmitButton"] > button[kind="tertiary"] {
                color: #273450 !important;
                -webkit-text-fill-color: #273450 !important;
                background: #edf0f8 !important;
                border-color: #d8dfed !important;
            }

            div[data-testid="stButton"] > button[kind="primary"] *,
            div[data-testid="stFormSubmitButton"] > button[kind="primary"] *,
            div[data-testid="stDownloadButton"] > button *,
            div[data-testid="stButton"] > button[kind="secondary"] *,
            div[data-testid="stFormSubmitButton"] > button[kind="secondary"] * {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
            }

            div[data-testid="stButton"] > button[kind="tertiary"] * {
                color: #273450 !important;
                -webkit-text-fill-color: #273450 !important;
            }

            [data-testid="stLinkButton"] a {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
                background: linear-gradient(135deg, #4659d4, #3647b5) !important;
                border-color: transparent !important;
                border-radius: 13px !important;
                font-weight: 700 !important;
            }

            [data-testid="stLinkButton"] a * {
                color: #fff !important;
                -webkit-text-fill-color: #fff !important;
            }

            div[data-testid="stButton"] > button:not(:disabled):hover,
            div[data-testid="stDownloadButton"] > button:not(:disabled):hover {
                transform: translateY(-1px);
                box-shadow: 0 10px 22px rgba(45, 60, 120, .18);
                border-color: rgba(83, 103, 245, .2) !important;
            }

            div[data-testid="stButton"] > button:focus-visible,
            div[data-testid="stDownloadButton"] > button:focus-visible,
            input:focus-visible, textarea:focus-visible,
            [data-baseweb="select"] > div:focus-within {
                outline: 3px solid rgba(79, 98, 232, .42) !important;
                outline-offset: 2px;
            }

            div[data-testid="stButton"] > button:active:not(:disabled),
            div[data-testid="stDownloadButton"] > button:active:not(:disabled) {
                transform: translateY(0);
            }

            div[data-testid="stButton"] > button:disabled,
            div[data-testid="stFormSubmitButton"] > button:disabled,
            div[data-testid="stDownloadButton"] > button:disabled {
                color: #46516a !important;
                -webkit-text-fill-color: #46516a !important;
                background: #e4e8f0 !important;
                border-color: #d4dbe7 !important;
                opacity: 1;
                box-shadow: none;
            }

            div[data-testid="stButton"] > button:disabled *,
            div[data-testid="stFormSubmitButton"] > button:disabled,
            div[data-testid="stFormSubmitButton"] > button:disabled *,
            div[data-testid="stDownloadButton"] > button:disabled,
            div[data-testid="stDownloadButton"] > button:disabled * {
                color: #46516a !important;
                -webkit-text-fill-color: #46516a !important;
            }

            input:not([type="checkbox"]):not([type="radio"]), textarea,
            [data-baseweb="select"] > div {
                border-radius: 12px !important;
                border-color: #dce3f0 !important;
                background-color: #fff !important;
                transition: border-color .18s ease, box-shadow .18s ease;
            }

            [data-testid="stTextInput"] input,
            [data-testid="stNumberInput"] input,
            [data-testid="stDateInput"] input,
            [data-testid="stTimeInput"] input,
            [data-testid="stPasswordInput"] input,
            [data-testid="stTextArea"] textarea,
            [data-baseweb="input"] input,
            [data-baseweb="textarea"] textarea {
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink) !important;
                background-color: #fff !important;
                caret-color: var(--brand-dark);
                opacity: 1 !important;
            }

            [data-baseweb="input"] > div,
            [data-baseweb="textarea"] > div,
            [data-testid="stTextInput"] [data-baseweb="input"],
            [data-testid="stNumberInput"] [data-baseweb="input"],
            [data-testid="stDateInput"] [data-baseweb="input"],
            [data-testid="stTimeInput"] [data-baseweb="input"],
            [data-testid="stPasswordInput"] [data-baseweb="input"],
            [data-testid="stTextArea"] [data-baseweb="textarea"] {
                background-color: #fff !important;
                border-color: #cbd4e3 !important;
            }

            [data-testid="stTextInput"] input::placeholder,
            [data-testid="stNumberInput"] input::placeholder,
            [data-testid="stDateInput"] input::placeholder,
            [data-testid="stTimeInput"] input::placeholder,
            [data-testid="stPasswordInput"] input::placeholder,
            [data-testid="stTextArea"] textarea::placeholder,
            [data-baseweb="input"] input::placeholder,
            [data-baseweb="textarea"] textarea::placeholder {
                color: #69758d !important;
                -webkit-text-fill-color: #69758d !important;
                opacity: 1 !important;
            }

            [data-baseweb="select"] [role="combobox"],
            [data-baseweb="select"] [role="combobox"] * {
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink) !important;
            }

            [data-baseweb="popover"],
            [data-baseweb="popover"] [role="listbox"],
            [data-baseweb="popover"] [role="option"] {
                color: var(--ink) !important;
                background-color: #fff !important;
            }

            [data-baseweb="popover"] *,
            [role="listbox"] *,
            [role="option"] * {
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink) !important;
            }

            [role="option"]:hover,
            [role="option"][aria-selected="true"] {
                background-color: #edf0f8 !important;
            }

            [data-testid="stTextInput"] input,
            [data-testid="stNumberInput"] input,
            [data-testid="stDateInput"] input,
            [data-testid="stTimeInput"] input,
            [data-baseweb="select"] > div {
                min-height: 2.85rem;
            }

            input:focus, textarea:focus, [data-baseweb="select"] > div:focus-within {
                border-color: var(--brand) !important;
                box-shadow: 0 0 0 3px rgba(83, 103, 245, .12) !important;
            }

            [data-testid="stFileUploader"],
            [data-testid="stCameraInput"],
            [data-testid="stAudioInput"],
            [data-testid="stSelectbox"] {
                border-radius: 16px;
            }

            [data-testid="stFileUploader"] section {
                border: 1px dashed #cbd4e6;
                border-radius: 14px;
                background: #f8faff;
            }

            [data-testid="stAlert"] {
                border-radius: 14px;
                border: 1px solid rgba(83, 103, 245, .12);
            }

            [data-testid="stAlert"] p,
            [data-testid="stAlert"] span,
            [data-testid="stAlert"] li,
            [data-testid="stAlert"] [data-testid="stMarkdownContainer"] {
                color: #26334d !important;
            }

            [data-testid="stFileUploader"] *,
            [data-testid="stCameraInput"] *,
            [data-testid="stAudioInput"] * {
                color: var(--ink);
            }

            [data-testid="stCaptionContainer"] {
                font-size: .9rem;
                line-height: 1.5;
            }

            [data-testid="stDataFrame"], [data-testid="stTable"] {
                overflow: hidden;
                border: 1px solid var(--line);
                border-radius: 14px;
                background: #fff;
                color: var(--ink);
            }

            [data-testid="stTable"] th,
            [data-testid="stTable"] td,
            [data-testid="stTable"] [data-testid="stMarkdownContainer"] {
                color: var(--ink) !important;
            }

            [data-testid="stCode"] {
                color: #edf2ff;
                background-color: #17213d;
                border-radius: 12px;
            }

            [data-testid="stImage"] img {
                border-radius: 16px;
            }

            [data-testid="stDialog"] > div,
            [role="dialog"] > div {
                border: 1px solid var(--line);
                border-radius: 22px;
                color: var(--ink) !important;
                background: #fff !important;
                box-shadow: 0 24px 80px rgba(18, 28, 69, .24);
            }

            [data-testid="stDialog"] p,
            [data-testid="stDialog"] li,
            [data-testid="stDialog"] label,
            [data-testid="stDialog"] [data-testid="stMarkdownContainer"],
            [role="dialog"] p,
            [role="dialog"] li,
            [role="dialog"] label,
            [role="dialog"] [data-testid="stMarkdownContainer"] {
                color: var(--ink) !important;
            }

            [data-testid="stDialog"] [data-testid="stVerticalBlockBorderWrapper"],
            [role="dialog"] [data-testid="stVerticalBlockBorderWrapper"] {
                box-shadow: none;
            }

            hr, [data-testid="stDivider"] {
                border-color: var(--line) !important;
            }

            [data-testid="stSpinner"] > div { border-top-color: var(--brand) !important; }

            @media (max-width: 700px) {
                .block-container {
                    width: min(100% - 1.25rem, 1160px);
                    padding-top: 1.1rem !important;
                }

                .brand img { height: 58px; }
                .brand--home img { height: 76px; }
                .brand--home h1 { font-size: clamp(1.7rem, 7vw, 2.4rem) !important; }
                .brand--dashboard h2 { font-size: 1.05rem !important; }

                div[data-testid="stButton"] > button {
                    padding: .5rem .75rem !important;
                }
            }

            @media (hover: none) {
                .subject-card:hover {
                    transform: none;
                    box-shadow: 0 8px 24px rgba(35, 48, 94, .06);
                }
            }

            @media (prefers-reduced-motion: reduce) {
                html { scroll-behavior: auto !important; }

                *, *::before, *::after {
                    scroll-behavior: auto !important;
                    animation-duration: .01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: .01ms !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
