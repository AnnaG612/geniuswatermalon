import time

import streamlit as st

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()  # Record the start time

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("HUSTDecoding Game")
st.write("Welcome to the HUST Decoding Challenge! Solve each layer to uncover the hidden message.")

if st.button("Reset Game"):
    st.session_state.step = 1

# Step 1: Marketing Trivia
if st.session_state.step == 1:
    st.subheader("Layer 1: Marketing Trivia")
    question = "Which framework is known as the 4Ps of marketing?"
    options = ["Porter's Five Forces", "SWOT Analysis", "Marketing Mix"]
    answer = st.radio(question, options)

    if st.button("Submit Answer"):
        if answer == "Marketing Mix":
            st.success("Correct! Proceeding to Layer 2...")
            st.session_state.step = 2
        else:
            st.error("Incorrect! Try again.")

# Step 2: Marketing Journals Quiz
if st.session_state.step == 2:
    st.subheader("Layer 2: Marketing Journals Quiz")
    st.write("Identify which of the following journals are about marketing. Select all that apply:")

    journals = [
        "Journal of Marketing",
        "Journal of Consumer Research",
        "Journal of Finance",
        "Harvard Business Review",
        "Journal of Psychology",
        "Marketing Science",
        "Nature",
        "Journal of Management",
        "Strategic Management Journal",
        "Journal of Advertising"
    ]

    correct_answers = {"Journal of Marketing", "Journal of Consumer Research", "Marketing Science", "Journal of Advertising"}
    selected = st.multiselect("Select the marketing journals:", journals)

    if st.button("Submit Journals"):
        if set(selected) == correct_answers:
            st.success("Correct! Proceeding to Layer 3...")
            st.session_state.step = 3
        else:
            st.error("Incorrect! Try again.")

# Step 3: Case Study Challenge
if st.session_state.step == 3:
    st.subheader("Layer 3: Case Study Challenge")
    st.write("Match the following case studies with their descriptions:")

    cases = {
        "Apple": "This brand created the 'Think Different' campaign.",
        "Coca-Cola": "This brand leveraged emotional marketing to connect with consumers.",
        "Amazon": "This brand is known for its customer-centric approach and Prime membership."
    }

    user_inputs = {}
    for case, clue in cases.items():
        user_inputs[case] = st.text_input(f"Clue: {clue}", key=case)

    if st.button("Submit Case Studies"):
        correct_cases = {"Apple": "Apple", "Coca-Cola": "Coca-Cola", "Amazon": "Amazon"}
        if all(user_inputs[case] == correct_cases[case] for case in cases):
            st.success("Correct! Proceeding to Layer 4...")
            st.session_state.step = 4
        else:
            st.error("Incorrect! Try again.")

# Step 4: Advanced Decoding
from PIL import Image

# Updated Layer 4 with new Morse code answer
if st.session_state.step == 4:
    st.subheader("Layer 4: Advanced Decoding")
    st.write("Decode the hidden message using Morse code and an image transformation.")

    # Part 1: Morse Code Challenge
    st.write("Part 1: Decode this Morse code:")
    morse_code = "-- .- .-. -.- . - .. -. --."  # Morse code for "MARKETING"
    st.write(f"Morse Code: {morse_code}")
    morse_input = st.text_input("Enter the decoded Morse code:")

    # Part 2: Image Transformation Challenge
    st.write("Part 2: Decode the following image into the correct 7 alphabets (Hint: 🏠☂️🌟🌴📈🔑🌴).")

    # Display the image
    image_path = "hidden_text_image.png"  # Ensure the file is in the same directory as your code
    try:
        image = Image.open(image_path)
        st.image(image, caption="What's the hidden text?")
    except FileNotFoundError:
        st.error("Image file not found! Please check the file path.")

    # Accept user input for the image decoding
    image_input = st.text_input("Enter the 7 alphabets (in capital letters):")

    if st.button("Submit Decoding"):
        # Check both Morse code and image input
        if morse_input.upper() == "MARKETING" and image_input.upper() == "HUSTMKT":
            st.success("Congratulations! You've decoded the entire message!")
            st.session_state.step = 5
        else:
            st.error("Incorrect! Try again.")

# Layer 5: Game Completion and Celebration
if st.session_state.step == 5:
    st.subheader("🎉 Congratulations! You've Completed the Game! 🎉")

    # Display the banner message
    st.markdown(
        """
        <div style="text-align: center; padding: 20px; background-color: #f39c12; color: white; border-radius: 10px; font-size: 24px;">
            <strong>Join HUST Marketing! You are the one we've been looking for!</strong>
        </div>
        """,
        unsafe_allow_html=True
    )


    # Display the fireworks GIF
    gif_path = 'fireworks.gif'
    gif_image = Image.open(gif_path)
    st.image(gif_image, caption='Celebration Time!')

    # Display time taken
    end_time = time.time()
    elapsed_time = end_time - st.session_state.start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    st.write(f"⏱️ You completed the game in {minutes} minutes and {seconds} seconds!")