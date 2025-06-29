simport streamlit as st
st.title("AESTHETIC HEALTH/BEAUTY BY KUNAL TRIPATHI")
st.header("fill the form to connect with our experts")
name = st.text_input("enter your name")
phone_number = st.text_input("enter your phone number")
email = st.text_input("enter your email")
service = st.text_input("enter your service")
button = st.button("book free consultation")
if button:
    st.markdown(f"""
                name: {name}
                phone_number: {phone_number}
                email: {email}
                service: {service}""")
