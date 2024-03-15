import streamlit as st

st.header("Quiz")
st.subheader("Choose a quiz:")

if st.button("world quiz"):
    st.switch_page("pages/world_quiz.py")
if st.button("book quiz"):
    st.switch_page("pages/book_quiz.py")
