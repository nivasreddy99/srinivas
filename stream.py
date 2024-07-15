import streamlit as st

st.title("Hello World")

st.write("This is a simple Hello World application using Streamlit.")

st.info("This app is built using Python and Streamlit.")

st.success("The app has been successfully deployed.")

st.warning("Please note that this is a demo application and does not connect to any external APIs or databases.")

st.error("An error occurred while fetching data.")
st.chat_message("An error occurred while fetching data")
st.code("An error occurred while fetching data")

st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Cat_with_teeth.jpg/220px-Cat_with_teeth.jpg")

st.table([
    {"Name": "John", "Age": 30},
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 35}])

st.slider("Slider", min_value=0, max_value=100, value=50)

st.selectbox("Select box", ["Option 1", "Option 2", "Option 3"])

st.multiselect("Multi-select box", ["Option 1", "Option 2", "Option 3"])    

st.radio("Radio button", ["Option 1", "Option 2", "Option 3"])

st.checkbox("Checkbox")

st.text_area("Text area")

st.text_input("Text input")

st.number_input("Number input") 

st.date_input("Date input")

st.time_input("Time input")

st.color_picker("Color picker")

    # Your application code here 