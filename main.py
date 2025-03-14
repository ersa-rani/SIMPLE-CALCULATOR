import streamlit as st

def main():
    st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
    
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🧮 Simple Calculator")
    st.markdown("### Enter two numbers and select an operation")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            num1 = st.number_input("Enter first number", value=0.0, step=1.0)

        with col2:
            num2 = st.number_input("Enter second number", value=0.0, step=1.0)

    operations = {
        "➕ Addition": "+",
        "➖ Subtraction": "-",
        "✖️ Multiplication": "*",
        "➗ Division": "/"
    }

    operation = st.selectbox("Select an operation", list(operations.keys()))

    if st.button("Calculate"):
        try:
            if operation == "➕ Addition":
                result = num1 + num2
            elif operation == "➖ Subtraction":
                result = num1 - num2
            elif operation == "✖️ Multiplication":
                result = num1 * num2
            elif operation == "➗ Division":
                if num2 == 0:
                    st.error("❌ ERROR: Division by zero is not allowed")
                    return
                result = num1 / num2

            st.success(f"**Result:** {num1} {operations[operation]} {num2} = {result}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
