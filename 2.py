import streamlit as st
import math

st.title("AYALKBET Scientific Calculator")

expression = st.text_input("Enter Expression")

if st.button("Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except:
        st.error("Invalid expression")

# Extra functions
if st.button("Square Root"):
    try:
        val = float(expression)
        st.success(math.sqrt(val))
    except:
        st.error("Invalid input")

if st.button("Factorial"):
    try:
        val = int(float(expression))
        st.success(math.factorial(val))
    except:
        st.error("Only non-negative integers allowed")