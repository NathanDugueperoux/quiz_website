import streamlit as st

st.markdown("# world quiz")
st.write("")
question_1 = st.radio("What is the capital city of England?",
                      ["London",
                       "Paris",
                       "Berlin",
                       "New Delhi"])
question_2 = st.radio("What is the capital city of France?",
                      ["London",
                       "Paris",
                       "Berlin",
                       "New Delhi"])
question_3 = st.radio("What is the capital city of India?",
                      ["London",
                       "Paris",
                       "Berlin",
                       "New Delhi"])
question_4 = st.radio("What is the capital city of Germany?",
                      ["London",
                       "Paris",
                       "Berlin",
                       "New Delhi"])
questions = [question_1, question_2, question_3, question_4]
right_answers = ["London", "Paris", "New Delhi", "Berlin"]
submit = st.button("Submit")
if submit:
    score = 0
    for i in range(len(questions)):
        if questions[i] == right_answers[i]:
            score += 1
    st.markdown(f"You got {score}/4.")
