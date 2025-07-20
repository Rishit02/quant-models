import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Explore different models for modelling financial instruments.
    """
)