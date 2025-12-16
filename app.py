import streamlit as st
from ai_agent import generate_test_steps
from selenium_runner import run_test
from evaluation_layer import evaluate

st.title("Agentic AI QA Engineer")

requirement = st.text_area(
    "Enter software requirement:",
    "User should not be able to login with wrong password"
)

test_url = st.text_input(
    "Enter website URL to test:",
    "http://localhost:8000"
)

if st.button("Run AI QA Test"):
    steps = generate_test_steps(requirement)
    st.subheader("Generated Test Steps")
    st.json(steps)

    result, reason = run_test(steps, test_url)
    st.subheader("Test Result")
    st.write(result)

    explanation = evaluate(result, reason)
    st.subheader("AI Explanation")
    st.write(explanation)