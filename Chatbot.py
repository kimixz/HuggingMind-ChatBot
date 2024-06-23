import streamlit as st
import openai
import base64
import presidio_analyzer as pres_analyzer
import presidio_anonymizer as pres_anonymizer


openai.api_key = st.secrets['OPENAI_API_KEY']
st.set_page_config(
    page_title="HuggingMind Bot",
    page_icon="./assets/huggingmind_chat_icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.session_state["model"] = st.secrets['OPENAI_FINETUNED_MODEL']
st.session_state["assistant_id"] = st.secrets['OPENAI_ASSISTANT_KEY']
st.title("HuggingMind Bot")
st.warning("⚠️ HuggingMind Bot is not intended to replace professional mental health advice, diagnosis, treatment, or crisis support. You're not required to provide personal information except the name of your university. ")

client = openai.OpenAI(
        api_key=openai.api_key,
    )

# Function to convert image to base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


with st.sidebar:
    img_path = "./assets/HuggingMind.svg"  
    img_base64 = img_to_base64(img_path)
    st.markdown(
        f'<img src="data:image/svg+xml;base64,{img_base64}" style="width:100%; height:auto;">',
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown("""\nHuggingMind is an AI-driven mental health chatbot provides university 
students with 24/7 personalized support, utilizing advanced language models and university-specific mental health resources.
""")
    st.error("Your data privacy is our top priority. We do not store your conversation history nor your personal information you might have accidently put in our chat platform.")
 
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:  
    if message['role'] == 'user':
        avatar_path = './assets/user_icon.png'
    else:
        avatar_path = './assets/huggingmind_chat_icon.png'

    with st.chat_message(message['role'], avatar=avatar_path):
        st.markdown(message["content"])

def anonymize_user_input(user_input):
    analyzer = pres_analyzer.AnalyzerEngine()
    anonymizer = pres_anonymizer.AnonymizerEngine()
    results = analyzer.analyze(text=user_input, entities=['PERSON', 'CREDIT_CARD', 'IP_ADDRESS', 'EMAIL_ADDRESS', 'PHONE_NUMBER'], language='en')
    anonymized_text = anonymizer.anonymize(text=user_input,analyzer_results=results)

    return results, anonymized_text.text

def submit_chat(user_input):
    thread = client.beta.threads.create()
    message_format = {"role": "user", "content": user_input}
    st.session_state.messages.append(message_format)
    with st.chat_message("user",avatar='./assets/user_icon.png'):
        st.markdown(user_input)
    
    results, anonymized_input = anonymize_user_input(user_input)
    for result in results:
        if result.entity_type == "PERSON":
            name = user_input[result.start:result.end]
            if len(name.split(" ")) == 2:
                name = name.split(" ")[0]   # only take the first name
    print(anonymized_input)
    print(results)
    message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=anonymized_input
            )

    with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=st.session_state["assistant_id"]
    ) as stream:
        assistant_response = st.chat_message("assistant", avatar='./assets/huggingmind_chat_icon.png').empty()
        full_response = ""
        for event in stream:
        # Print the text from text delta events
            if event.event == "thread.message.delta" and event.data.delta.content:
                full_response += event.data.delta.content[0].text.value
                if "<PERSON>" in full_response:
                    full_response = full_response.replace("<PERSON>", name)
                assistant_response.write(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})


def main():
    if prompt := st.chat_input("Have a conversation with me :)"):
        submit_chat(prompt)


if prompt := st.chat_input("Have a conversation with me :)"):
    submit_chat(prompt)


