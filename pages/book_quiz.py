import streamlit as st

st.markdown("# book quiz")
st.write("")
question_1 = st.radio("Who wrote Harry Potter?", ["Nathan Dugueperoux",
                                                  "J K Rowling",
                                                  "Stephen King",
                                                  "William Shakespeare"])
question_2 = st.radio("What is famous a famous american author ?", ["Nathan Dugueperoux",
                                                                    "J K Rowling",
                                                                    "Stephen King",
                                                                    "William Shakespeare"])
question_3 = st.radio("Who has writen no books in his entire life?", ["Nathan Dugueperoux",
                                                                      "J K Rowling",
                                                                      "Stephen King",
                                                                      "William Shakespeare"])
question_4 = st.radio("Who wrote Hamlet?", ["Nathan Dugueperoux",
                                            "J K Rowling",
                                            "Stephen King",
                                            "William Shakespeare"])

questions = [question_1, question_2, question_3, question_4]
right_answers = ["J K Rowling", "Stephen King", "Nathan Dugueperoux", "William Shakespeare"]
submit = st.button("Submit")
if submit:
    score = 0
    for i in range(len(questions)):
        if questions[i] == right_answers[i]:
            score += 1
    st.markdown(f"You got {score}/4.")
