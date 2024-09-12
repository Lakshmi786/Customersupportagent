import streamlit as st

st.set_page_config(layout = 'wide', page_title = 'Retail Chatbot', page_icon = '👗')

if 'message_history' not in st.session_state:
    st.session_state.message_history = [{'content' :  "Hi , I am the your fashion expert bot. How can i help you?", 'type': 'assistant'}]

left_col , main_col, right_col = st.columns([1,2,1])

# 1. Button for chat - Clear Button
with left_col:
    if st.button('Clear'):
        st.session_state.message_history = []

# 2. chat history and input
with main_col:
    user_input = st.chat_input('Type here')

    if user_input:
        st.session_state.message_history.append({'content' : user_input , 'type': 'user'})
    
    for i in range(1, len(st.session_state.message_history) + 1):
        this_message = st.session_state.message_history[-i]
        message_box = st.chat_message(this_message['type'])
        message_box.markdown(this_message['content'])

# 3. State Variables
with right_col:
    st.text(st.session_state.message_history)