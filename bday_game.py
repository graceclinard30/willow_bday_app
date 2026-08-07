import streamlit as st
import random as rd

name = "Willow"

st.header("HAPPY BIRTHDAY " + name.upper()+ "!!!")

##Do you want to play?/ Form
with st.form("play_form"):
    play_response = st.text_input("I made you this puzzle/riddle website. Wanna play?")

    play_submit = st.form_submit_button("Submit Answer")

if play_submit == True:
    if play_response.lower() in ("Yes","yes","Yeah","YEAH","YES","yeah","Yep"):
        st.success("GREAT! No is not an option") st.balloons()
    else:
        st.error("You meant to say Yes")

##First Question
with st.form("first_q"):
    first_q = st.radio(f"""I have no lungs, yet I can breathe.\n
    I have no legs, yet through halls I creep.\n
    I carry secrets from witch to wizard,\n
    And disappear when my message is heard.\n
    What am I?""",["An Owl","A ghost","A Spell","A Patronus Message"])

    first_q_submit = st.form_submit_button("Submit")

if first_q_submit == True:
    if first_q == "A Patronus Message":
        st.success("YOU'RE A WIZARD, HARRY")
    else:
        st.error("What kind of Harry Potter fan are you?!?!?! Try again")

##Second Question

# with st.form("Number Guess"):
#     st.write("Pick a number from 1-100, I am going to try and guess the number you chose in 6 tries. If I get it wrong, tell me if I went too high or too low. If I get it right, choose correct.")
#     submit_guess = st.form_submit_button("Generate Initial Guess")
#     if submit_guess:
#         random_guess = rd.randint(0,100)
#         st.write(f"My first guess is {random_guess}")

# tries = 0
# evaluation = st.pills("",["Correct","Too High","Too Low"])

# if evaluation == "Correct":
#     tries += 1
#     st.write(f"I guessed the number in {tries} tries!")
# elif evaluation == "Too High":
#     random_guess = rd.randint(0,random_guess)
#     st.write(f"Was it {random_guess}?")


if "minimum" not in st.session_state:
    st.session_state.minimum = 1

if "maximum" not in st.session_state:
    st.session_state.maximum = 100

if "random_guess" not in st.session_state:
    st.session_state.random_guess = None

if "tries" not in st.session_state:
    st.session_state.tries = 0


with st.form("Number Guess"):
    st.write(
        "Pick a number from 1-100. I will try to guess it in six tries."
    )

    submit_guess = st.form_submit_button("Generate Initial Guess")

    if submit_guess:
        st.session_state.minimum = 1
        st.session_state.maximum = 100
        st.session_state.tries = 1
        st.session_state.random_guess = rd.randint(1, 100)


if st.session_state.random_guess is not None:
    st.write(f"Is your number {st.session_state.random_guess}?")

    evaluation = st.pills(
        "Choose an answer:",
        ["Correct", "Too High", "Too Low"],
        key=f"evaluation_{st.session_state.tries}"
    )

    if evaluation == "Correct":
        st.success(
            f"I guessed your number in {st.session_state.tries} tries!"
        )

    elif evaluation == "Too High":
        st.session_state.maximum = st.session_state.random_guess - 1

        st.session_state.random_guess = rd.randint(
            st.session_state.minimum,
            st.session_state.maximum
        )

        st.session_state.tries += 1
        st.rerun()

    elif evaluation == "Too Low":
        st.session_state.minimum = st.session_state.random_guess + 1

        st.session_state.random_guess = rd.randint(
            st.session_state.minimum,
            st.session_state.maximum
        )

        st.session_state.tries += 1
        st.rerun()

# Do a game based on a dataset, do a 

st.image("Harry_Potter_Meme.webp")
