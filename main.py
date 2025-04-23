import streamlit as st

st.set_page_config(page_title="Unit Converter" , page_icon="▪")

st.title("UNIT CONVERTER")
st.markdown("# Convert Time, Weight, Height")
st.write("Welcome! This app converts unit of height, time and weight. ")
st.write("Please select the type and enter a value to get result instantly.")
type = st.selectbox("Which type you want to convert select here",["Weight","Length","Time"])

def converter(type, value, unit):
    if type == "Length":
        if unit == "Kilometer to Miles":
            return value * 0.621371
        elif unit == "Miles to Kiometer":
            return value / 0.621371
        
    elif type == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif type == "Time":
        if unit == " Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
if type == "Length":
    unit = st.selectbox("Select a unit",["Kilometer to Miles","Miles to Kiometer"])
elif type == "Weight":
    unit = st.selectbox("Select a unit",["Kilograms to Pounds","Pounds to Kilograms"])
elif type == "Time":
    unit = st.selectbox("Select a unit",["Seconds to Minutes","Minutes to Seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])

value = st.number_input("Enter a value to convert")

if st.button('Convert'):
    result = converter(type, value, unit)
    st.success(f"The result is {result:.2f}")
