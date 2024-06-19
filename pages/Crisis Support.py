import streamlit as st

# Adding custom CSS for enhanced styling
st.markdown("""
    <style>
    :root {
        --background-color-light: #eee;
        --background-color-dark: #333;
        --highlight-light: #FFCCCB;
        --highlight-dark: #ff5252;
        --text-color-light: #333;
        --text-color-dark: #fff;
        --header-color-light: #4CAF50;
        --header-color-dark: #8BC34A;
        --footer-color-light: #666;
        --footer-color-dark: #ccc;
        --link-color-light: #1E90FF;
        --link-color-dark: #87CEFA;
        --link-color-light: #007BFF;
        --link-color-dark: #00BFFF;
    }

    @media (prefers-color-scheme: light) {
        .highlight-container {
            background-color: var(--highlight-light);
            color: var(--text-color-light);
        }
        .crisis-support-container {
            background-color: var(--background-color-light);
            color: var(--text-color-light);
        }
        .highlight-container a {
            color: var(--link-color-light);
        }
        .crisis-support-container a {
            color: var(--link-color-light);
        }
        .crisis-support-container ul li strong {
            color: var(--text-color-light);
        }
        .footer {
            color: var(--footer-color-light);
        }
    }

    @media (prefers-color-scheme: dark) {
        .highlight-container {
            background-color: var(--highlight-dark);
            color: var(--text-color-dark);
        }
        .crisis-support-container {
            background-color: var(--background-color-dark);
            color: var(--text-color-dark);
        }
        .highlight-container a {
            color: var(--link-color-dark);
        }
        .crisis-support-container a {
            color: var(--link-color-dark);
        }
        .crisis-support-container ul li strong {
            color: var(--text-color-dark);
        }
        .footer {
            color: var(--footer-color-dark);
        }
    }
            
    .highlight-container {
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .crisis-support-container {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .crisis-support-container h5 {
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .crisis-support-container ul {
        list-style-type: disc;
        padding-left: 10px;
    }
    .crisis-support-container ul li {
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
    st.info("Important crisis support information for immediate help and mental health resources.")

# Main content
st.title("☎️ Crisis Support")

# Crisis support container
st.markdown("""
<div class="highlight-container">
    <h5>⚠️ If you're in immediate danger or need urgent help, call <a href="tel:9-1-1">9-1-1</a>.</strong></h5>
    <h5>⚠️ If you or someone you know think about suicide, call or text <a href="https://988.ca/">9-8-8</a>.</strong></h5>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="crisis-support-container">
    <h5>Support for First Nations, Inuit, and Métis Peoples</h5>
    <ul>
        <li><strong>Hope for Wellness Help Line:</strong> Call <a href="tel:1-855-242-3310">1-855-242-3310</a> (toll-free) or connect to the <a href="https://www.hopeforwellness.ca/">online Hope for Wellness chat</a>. Support is available in English and French and, by request, in Cree, Ojibway, and Inuktitut.</li>
        <li><strong>The National Indian Residential School Crisis Line:</strong> Crisis support is available to former Indian Residential School students and their families 24 hours a day, 7 days a week at <a href="tel:1-866-925-4419">1-866-925-4419</a> (toll-free).</li>
        <li><strong>Missing and Murdered Indigenous Women and Girls Crisis Line:</strong> Crisis support is available to individuals impacted by the issue of missing and murdered Indigenous women, girls, and 2SLGBTQQIA+ people 24 hours a day, 7 days a week at <a href="tel:1-844-413-6649">1-844-413-6649</a> (toll-free).</li>
    </ul>
    <h5>Support for Youth and Young Adults</h5>
    <ul>
        <li><strong>Kids Help Phone:</strong> Call <a href="tel:1-800-668-6868">1-800-668-6868</a> (toll-free) or text CONNECT to <a href="sms:686868">686868</a>. Available 24 hours a day, 7 days a week to Canadians aged 5 to 29 who want confidential and anonymous care from trained responders.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer with call-to-action
st.markdown("""
<div class="footer">
    <p>Don't hesitate to reach out for help. Support is available 24/7.</p>
</div>
""", unsafe_allow_html=True)
