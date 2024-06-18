import streamlit as st
import openai
import base64
openai.api_key = st.secrets['OPENAI_API_KEY']
st.session_state["model"] = st.secrets['OPENAI_FINETUNED_MODEL']
st.session_state["assistant_id"] = "asst_lYoJwmKMp7oALbM5XT36rHDe"
st.title("Mental Health Chatbot")

client = openai.OpenAI(
        api_key=openai.api_key,
    )



# INITIAL_MESSAGE = {
#         "role": "assistant",
#         "content": "Hey there, I'm Mental Health Chatbot! How can I help you today?",
#     }
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    # st.session_state.messages.append(INITIAL_MESSAGE)
def display_chat_history():
    for message in st.session_state.messages:
        print(message)
        with st.chat_message(message['role']):
            st.markdown(message["content"])

thread = client.beta.threads.create()
def submit_chat(user_input):
    
    message_format = {"role": "user", "content": user_input}
    st.session_state.messages.append(message_format)

    message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
            )
    run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=st.session_state["assistant_id"],
            )
    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
    print(messages)
    print(messages[0].content[0].text.value)
    assistant_response = {"role": "assistant", "content": messages[0].content[0].text.value}
    st.session_state.messages.append(assistant_response)
    return messages[0].content[0].text.value
def main():
    if prompt := st.chat_input("Have a conversation with me :)"):
        submit_chat(prompt)
        display_chat_history()

main()
