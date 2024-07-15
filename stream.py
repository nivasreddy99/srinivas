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

if __name__ == "__main__":
    st.cache(allow_output_mutation=True)
    # Your application code here 