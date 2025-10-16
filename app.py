import streamlit as st

# App title
st.title("🧮 Simple Calculator App")
st.write("Perform basic arithmetic operations easily!")

# Input numbers
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Division by zero is not allowed!")
