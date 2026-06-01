from ai_analyzer import (
    analyze_with_ai
)
import streamlit as st

from ai_analyzer import analyze_with_ai

st.set_page_config(
    page_title="ScamShield AI",
    layout="wide"
)

st.title("🛡 ScamShield AI")

st.caption(
    "Protect your time, money, and career."
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛡 Scam Detector",
    "📈 Opportunity Analyzer",
    "🎯 Career Validator",
    "📜 Certification Checker",
    "🔥 Roast My Plan"
])

# TAB 1

with tab1:

    st.header("🛡 Scam Detector")

    text = st.text_area(
        "Paste message, email, job offer, internship offer or website text"
    )

    if st.button("Analyze Scam"):

        with st.spinner("Analyzing..."):

            result = analyze_with_ai(
                "Scam Detection",
                text
            )

        st.markdown(result)
# TAB 2

with tab2:

    st.header("📈 Opportunity Analyzer")

    text = st.text_area(
        "Describe the opportunity"
    )

    if st.button("Analyze Opportunity"):

        with st.spinner("Analyzing..."):

            result = analyze_with_ai(
                "Opportunity Analysis",
                text
            )

        st.markdown(result)
# TAB 3

with tab3:

    st.header("🎯 Career Validator")

    text = st.text_area(
        "Describe your goal, current skills and plan"
    )

    if st.button("Validate Career Plan"):

        with st.spinner("Analyzing..."):

            result = analyze_with_ai(
                "Career Validation",
                text
            )

        st.markdown(result)
# TAB 4

with tab4:

    st.header("📜 Certification Checker")

    text = st.text_area(
        "Paste certification details"
    )

    if st.button("Analyze Certification"):

        with st.spinner("Analyzing..."):

            result = analyze_with_ai(
                "Certification Evaluation",
                text
            )

        st.markdown(result)

# TAB 5

with tab5:

    st.header("🎯 Reality Check AI")

    text = st.text_area(
        "Describe your goal and plan"
    )

    if st.button("Reality Check"):

        with st.spinner("Analyzing..."):

            result = analyze_with_ai(
                "Reality Check",
                text
            )

        st.markdown(result)