import streamlit as st

# Set up the page
st.set_page_config(
    page_title="My first app",
    layout="centered", # or 'wide'
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

# Title
st.title("What's Your Superhero Name?")

# User Inputs
fav_colour = st.text_input("What is your favourite colour?")

fav_animal = st.text_input("What is your favourite animal?")

lucky_num = st.number_input("What is your lucky number?", step=1)

#Dropdown for superpower
superpower = st.selectbox("Choose an option:", ["flying", "invisibility", "super strength", "teleportation"])


# Generate superhero name on button click
if st.button("Generate my superhero name") == True:
    superhero_name = f"{fav_colour} {fav_animal} of {lucky_num}"
    st.header(f"Your superhero name: {superhero_name}")
    st.write(f"Superpower: {superpower}")

    # Display motto