import streamlit as st

st.title("☕ Coffee Order App")

# Select coffee type
coffee_type = st.selectbox("Choose your coffee:", ["","Espresso", "Latte", "Cappuccino", "Americano", "Mocha"])
# Select size
size = st.radio("Select size:", ["Small", "Medium", "Large"])

# Add-ons
milk = st.checkbox("Add Milk")
sugar = st.checkbox("Add Sugar")
extra_shot = st.checkbox("Extra Espresso Shot")

# Submit button
if st.button("Place Order"):
    st.success(f"Order placed: {size} {coffee_type}")
    if milk or sugar or extra_shot:
        st.write("Add-ons:")
        if milk: st.write("- Milk")
        if sugar: st.write("- Sugar")
        if extra_shot: st.write("- Extra Shot")