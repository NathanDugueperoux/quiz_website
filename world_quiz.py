import streamlit as st

st.header("World quiz")
st.write("")
question_1 = st.radio("What is the capital city of England?", ["London", "Paris", "Berlin", "New Dehli"])
question_2 = st.radio("What is the capital city of France?", ["London", "Paris", "Berlin", "New Dehli"])
questions = [question_1, question_2]
right_answers = ["London", "Paris"]
submit = st.button("Submit")
if submit:
    score = 0
    for i in range(len(questions)):
        if questions[i] == right_answers[i]:
            score += 1
    st.markdown(f"You got {score}/2.")

