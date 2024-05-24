import streamlit as st
import LangchainSupport

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", (
    "Italian", "Chinese", "Indian", "Mexican", " French", "Japanese", "Thai", "Greek", "Spanish", "Lebanese", "Turkish",
    "Korean", "Vietnamese", " Moroccan", "Ethiopian", "Brazilian", "Peruvian", "Caribbean"))

if cuisine:
    response = LangchainSupport.restaurant_name_generator(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items:")
    for item in menu_items:
        st.write("-", item)
