import streamlit as st
import main
import time

st.title("CodeBro-ChatBot")

user_message = st.chat_input("Type your message", max_chars=500 )

toggle = st.toggle("Click Here, For Thinking Mode")

if toggle:
    main.toggle("On")
else:
    main.toggle("Off")

if user_message:
    if toggle == False:
        usr_input = st.write(f"You said: {user_message}")
        st.write(f"Ai: {main.get_reply(user_message)}")
        st.success("Done")
    else:
        usr_input = st.write(f"You said: {user_message}")
        with st.spinner("Thinking", show_time=True):
            time.sleep(2)
        st.write(f"Ai: {main.get_reply(user_message)}")
        st.success("Done")







   


    