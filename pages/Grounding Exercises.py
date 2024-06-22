import streamlit as st
import base64

st.set_page_config(
    page_title="HuggingMind Bot",
    page_icon="./assets/huggingmind_chat_icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.session_state["model"] = st.secrets['OPENAI_FINETUNED_MODEL']
st.session_state["assistant_id"] = st.secrets['OPENAI_ASSISTANT_KEY']

# Function to convert image to base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
# Sidebar content
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

# Adding custom CSS for enhanced styling
st.markdown("""
    <style>
    :root {
        --background-color-light: #eee;
        --background-color-dark: #333;
        --text-color-light: #333;
        --text-color-dark: #fff;
        --header-color-light: #4CAF50;
        --header-color-dark: #8BC34A;
        --footer-color-light: #666;
        --footer-color-dark: #ccc;
        --link-color-light: #007BFF;
        --link-color-dark: #00BFFF;
    }

    @media (prefers-color-scheme: light) {
        .grounding-container {
            background-color: var(--background-color-light);
            color: var(--text-color-light);
        }
        .grounding-container a {
            color: var(--link-color-light);
        }
        .grounding-container ul li strong {
            color: var(--text-color-light);
        }
        .footer {
            color: var(--footer-color-light);
        }
    }

    @media (prefers-color-scheme: dark) {
        .grounding-container {
            background-color: var(--background-color-dark);
            color: var(--text-color-dark);
        }
        .grounding-container a {
            color: var(--link-color-dark);
        }
        .grounding-container ul li strong {
            color: var(--text-color-dark);
        }
        .footer {
            color: var(--footer-color-dark);
        }
    }
    .grounding-container {
        margin-top: 20px;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .grounding-container h3 {
        font-family: 'Arial', sans-serif;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .footer {
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.header("About")
    st.info("Here are some grounding methods to help you stay present and calm.")

# Main content
st.title("🌱 Grounding Exercises")

# Grounding methods container
st.markdown("""
<div class="grounding-container">
    <h3>Meditation</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/x0nZ1ZLephQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/>
    <h3>Deep Breathing Exercise</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DbDoBzGY3vo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/>
    <h3>5-4-3-2-1 Technique</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/30VMIEmA114" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/>
    <h3>Focus Reset Exercise</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/QtE00VP4W3Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/>
    <h3>Somatic Exercises</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/qxuDrgvXBTs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/>
    <h3>Relaxing Yoga</h3>
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/COp7BR_Dvps" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe><br/> 
</div>
""", unsafe_allow_html=True)

# Footer with call-to-action
st.markdown("""
<div class="footer">
    <p>Remember, grounding exercises can help you stay focused and calm.</p>
    <p>Take a moment to practice them regularly!</p>
</div>
""", unsafe_allow_html=True)
