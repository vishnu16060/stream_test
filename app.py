import streamlit as st
st.title("Take the input")
#Take a user imput
name=st.text_input("Enter your name:")

if st.button("submit"):
   st.write(f"print the name:{name}")
