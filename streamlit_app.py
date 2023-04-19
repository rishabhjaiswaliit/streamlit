import streamlit as st

st.title("Finding the largest among the 3 given numbers")
number1 = st.number_input('Insert a number')
number2 = st.number_input('Insert another number')
number3 = st.number_input('Insert yet another number')

st.write('The greatest number is: ', max(number1, number2, number3))  
