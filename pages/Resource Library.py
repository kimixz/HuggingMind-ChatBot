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
        .resource-library-container {
            background-color: var(--background-color-light);
            color: var(--text-color-light);
        }
        .resource-library-container a {
            color: var(--link-color-light);
        }
        .resource-library-container ul li strong {
            color: var(--text-color-light);
        }
        .footer {
            color: var(--footer-color-light);
        }
    }

    @media (prefers-color-scheme: dark) {
        .resource-library-container {
            background-color: var(--background-color-dark);
            color: var(--text-color-dark);
        }
        .resource-library-container a {
            color: var(--link-color-dark);
        }
        .resource-library-container ul li strong {
            color: var(--text-color-dark);
        }
        .footer {
            color: var(--footer-color-dark);
        }
    }

    .resource-library-container {
        margin-top: 20px;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }    
    .resource-library-container h3 {
        font-family: 'Arial', sans-serif;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .resource-library-container ul {
        list-style-type: disc;
        padding-left: 10px;
    }
    .resource-library-container ul li {
        font-size: 18px;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
    }
    .resource-library-container iframe {
        margin-top: 15px;
    }
    .footer {
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)
    
# Main content
st.title("📚 Resource Library")

# Resource library container
st.markdown("""
<div class="resource-library-container">
    <h3>Canada-wide services</h3> 
    <ul>
        <li><a href="https://www.canada.ca/en/health-canada/services/substance-use/get-help-with-substance-use.html" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Get help with substance use</a></li>  
        <li>Centre for Addiction and Mental Health (CAMH): <a href="https://moodle8.camhx.ca/moodle/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Free online courses</a></li> 
        <li>Canadian Mental Health Association (CMHA): <a href="https://cmha.ca/find-info/mental-health/general-info/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Mental health resources</a></li> 
    </ul><br/>
    <h3>Anxiety</h3> 
    <ul>
        <li><a href="https://adaa.org/understanding-anxiety" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Anxiety and Depression Association of America</a></li>
        <li><a href="https://www.helpguide.org/articles/stress/stress-management.htm" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Managing Stress</a></li>
        <li>Getting to Know Your Brain: Dealing with Stress
        <iframe width="850" height="450" src="https://www.youtube.com/embed/sTpo1FuYQ9I" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
        <li>Guided Visualization: Dealing with Stress
        <iframe width="850" height="450" src="https://www.youtube.com/embed/Dq9odPtHbcg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
    </ul><br/>
    <h3>Depression</h3> 
    <ul>
        <li>Behavioral Activation: Treatment of Adolescent Depression
        <iframe width="850" height="450" src="https://www.youtube.com/embed/1R6-gLZZhYc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
        <li><a href="https://www.nimh.nih.gov/health/topics/depression/index.shtml" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">Coping with Depression</a></li>
    </ul><br/>
    <h3>ADHD</h3> 
    <ul>
        <li>Mental Health Minute: Attention-Deficit/Hyperactivity Disorder
        <iframe width="850" height="450" src="https://www.youtube.com/embed/-j2PqoFCzX0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
    </ul><br/>
    <h3>Eating Disorders</h3> 
    <ul>
        <li>Mental Health Minute: Eating Disorders
        <iframe width="850" height="450" src="https://www.youtube.com/embed/_yM7_hbpRXc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
    </ul><br/>
    <h3>Bipolar Disorder</h3> 
    <ul>
        <li>Mental Health Minute: Bipolar Disorder in Adults
        <iframe width="850" height="450" src="https://www.youtube.com/embed/lOhelfEDAzs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
    </ul><br/>
    <h3>Mindfulness Meditation</h3> 
    <ul>
        <li>5-Minute Meditation You Can Do Anywhere
        <iframe width="850" height="450" src="https://www.youtube.com/embed/inpok4MKVLM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe></li>
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
