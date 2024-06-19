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
        .self-care-tips-container {
            background-color: var(--background-color-light);
            color: var(--text-color-light);
        }
        .self-care-tips-container a {
            color: var(--link-color-light);
        }
        .self-care-tips-container ul li strong {
            color: var(--text-color-light);
        }
        .footer {
            color: var(--footer-color-light);
        }
    }

    @media (prefers-color-scheme: dark) {
        .self-care-tips-container {
            background-color: var(--background-color-dark);
            color: var(--text-color-dark);
        }
        .self-care-tips-container a {
            color: var(--link-color-dark);
        }
        .self-care-tips-container ul li strong {
            color: var(--text-color-dark);
        }
        .footer {
            color: var(--footer-color-dark);
        }
    }

    .self-care-tips-container {
        margin-top: 20px;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .self-care-tips-container ul {
        list-style-type: disc;
        padding-left: 10px;
    }
    .self-care-tips-container ul li {
        font-size: 18px;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
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
    st.info("Here are some self-care tips to help you maintain your physical and mental well-being.")

# Main content
st.title("💡 Self-Care Tips")

# Self-care tips container
st.markdown("""
<div class="self-care-tips-container">
    <ul>
        <li><strong>Exercise Regularly.</strong> Aim for 30 minutes of walking daily to boost mood and health. Even small amounts of exercise are beneficial.</li>
        <li><strong>Eat a Balanced Diet.</strong> Maintain a balanced diet and drink plenty of water to enhance energy and focus. Monitor caffeine and alcohol intake as they can impact mood.</li>
        <li><strong>Prioritize Sleep.</strong> Stick to a sleep schedule, aim for 7-9 hours, and minimize blue light exposure before bedtime to improve sleep quality.</li>
        <li><strong>Engage in Hobbies.</strong> Make time for activities you enjoy, whether it's reading, crafting, playing music, or any other hobby that makes you happy.</li>
        <li><strong>Practice Mindfulness.</strong> Deep breathing exercises can help calm your mind and reduce stress. Try techniques like diaphragmatic breathing or box breathing.</li>
        <li><strong>Spend Time in Nature.</strong> Go for a walk in a park, hike in the woods, or simply sit outside to enjoy the fresh air and sunshine. Nature can have a calming effect on the mind.</li>
        <li><strong>Stay Connected.</strong> Reach out to friends or family members who can provide emotional support and practical help.</li>
        <li><strong>Seek Professional Help.</strong> If you&apos;re struggling with mental health issues, don&apos;t hesitate to seek help from a therapist or counselor.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer with call-to-action
st.markdown("""
<div class="footer">
    <p>Remember, taking care of yourself is a continuous journey.</p>
    <p>Stay positive and keep improving!</p>
</div>
""", unsafe_allow_html=True)
