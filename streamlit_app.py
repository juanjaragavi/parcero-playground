
import os
import taskingai
import streamlit as st
from taskingai.assistant import Assistant
from taskingai.assistant.chat import Chat

st.set_page_config(
    page_title="Welcome to Medellín! | MyParcero.com",
    page_icon="https://media.myparcero.com/favicon.ico",
    layout="centered")

st.image(
    'https://media.myparcero.com/parcero-1.png')

st.title("💬 Hi! I'm Parcero.")

# CSS Styles
st.markdown(
    """
    <style>
    body, * {
        font-family: "League Spartan", sans-serif;
    }
    h1 {
        font-size: 1.8em;
        font-family: "League Spartan", sans-serif;
        font-weight: 600;
    }
    h2, h3 {
        font-family: "League Spartan", sans-serif;
        font-weight: 600;
    }
    p {
        font-family: "League Spartan", sans-serif;
    }
    img {
        margin-left: 0px 5px 0px 5px;
        border: 0;
        padding: 0;
        width: 200px;    
    }
    .st-emotion-cache-cnbvxy a {
        color: rgb(55,125, 34);
    }
    .st-emotion-cache-1dp5vir {
        position: absolute;
        top: 0px;
        right: 0px;
        left: 0px;
        height: 0.125rem;
        background-image: linear-gradient(90deg, rgb(55,125, 34), rgb(14, 165, 233));
        z-index: 999990;
    }
    .st-cx {
        background: linear-gradient(to right, rgb(55,125, 34) 0%, rgb(55,125, 34) 50%, rgba(172, 177, 195, 0.25) 50%, rgba(172, 177, 195, 0.25) 100%);
    }.st-d1 {
        background: linear-gradient(to right, rgb(55,125, 34) 0%, rgb(55,125, 34) 50%, rgba(172, 177, 195, 0.25) 50%, rgba(172, 177, 195, 0.25) 100%);
    }
    .st-cy {
        height: 2px;
    }
    .st-emotion-cache-1vzeuhh {
        -webkit-box-align: center;
        align-items: center;
        background-color: rgb(55,125, 34);
        border-radius: 100%;
        border-style: none;
        box-shadow: none;
        display: flex;
        height: 0.75rem;
        -webkit-box-pack: center;
        justify-content: center;
        width: 0.75rem;
    }
    .st-emotion-cache-10y5sf6 {
        font-family: "Source Code Pro", monospace;
        font-size: 14px;
        padding-bottom: 9.33333px;
        color: rgb(55,125, 34);
        top: -22px;
        position: absolute;
        white-space: nowrap;
        background-color: transparent;
        line-height: 1.6;
        font-weight: normal;
    }
    .st-emotion-cache-19rxjzo:hover {
        border-color: rgb(55,125, 34);
        color: rgb(55,125, 34);
    }
    .st-emotion-cache-19rxjzo:active {
        border-color: rgb(55,125, 34);
        color: rgb(55,125, 34);
    }
    .st-emotion-cache-19rxjzo:focus:not(:active) {
    border-color: rgb(55,125, 34);
    color: rgb(55,125, 34);
}
    .st-emotion-cache-19rxjzo {
        border-radius: 25px;
    }
    .st-do {
        border-top-color: rgb(55,125, 34);
    }
    .st-dm {
        border-bottom-color: rgb(55,125, 34);
    }
    .st-dn {
        border-right-color: rgb(55,125, 34);
    }
    .st-dl {
        border-left-color: rgb(55,125, 34);
    }
    .st-bh {
        padding-top: 0.6rem;
    }
    .st-emotion-cache-jmw8un {
        display: flex;
        width: 2rem;
        height: 2rem;
        flex-shrink: 0;
        border-radius: 0.5rem;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        background-color: rgb(55,125, 34);
        color: rgb(0, 0, 0);
    }
    .st-emotion-cache-bho8sy {
        display: flex;
        width: 2rem;
        height: 2rem;
        flex-shrink: 0;
        border-top-left-radius: 0.5rem;
        border-top-right-radius: 0.5rem;
        border-bottom-right-radius: 0.5rem;
        border-bottom-left-radius: 0.5rem;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        background-color: rgb(55,125, 34);
        color: rgb(255, 255, 255);
    }
    .st-emotion-cache-1ghhuty {
        display: flex;
        width: 2rem;
        height: 2rem;
        flex-shrink: 0;
        border-top-left-radius: 0.5rem;
        border-top-right-radius: 0.5rem;
        border-bottom-right-radius: 0.5rem;
        border-bottom-left-radius: 0.5rem;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        background-color: rgb(14, 165, 233);
        color: rgb(255, 255, 255);
    }
    .st-emotion-cache-4zpzjl {
        display: flex;
        width: 2rem;
        height: 2rem;
        flex-shrink: 0;
        border-radius: 0.5rem;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        background-color: rgb(14, 165, 233);
        color: rgb(256, 256, 256);
    }
    </style>
    """,
    unsafe_allow_html=True
)

taskingai_api_key = os.getenv("TASKINGAI_API_KEY")

taskingai.init(api_key=taskingai_api_key)

assistant_id = "X5lMkWCHZ1TtQeilMouDIL6B"

assistant: Assistant = taskingai.assistant.get_assistant(
    assistant_id=assistant_id,
)

chat: Chat = taskingai.assistant.create_chat(
    assistant_id=assistant_id,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome to Medellín! How can I help you today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    chat_response = taskingai.assistant.create_message(
        assistant_id=assistant.assistant_id,
        chat_id=chat.chat_id,
        text=prompt
    )

    assistant_message_response = taskingai.assistant.generate_message(
        assistant_id=assistant.assistant_id,
        chat_id=chat.chat_id,
        stream=False,
    )             

    msg = assistant_message_response.content.text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
