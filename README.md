# 🎈 HuggingMind Bot


## Overview of the App

HuggingMind is an AI-driven mental health chatbot provides university students with 24/7 personalized support and immediate access to professional guidance, utilizing advanced language models and university-specific mental health resources.

<img width="1263" alt="Screenshot 2024-08-13 at 5 14 19 PM" src="https://github.com/user-attachments/assets/fd62194b-ff80-4bd6-b9e5-edc96935acd9">



## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingmind.streamlit.app/)

### Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps, do the following:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API key into the text box as follows:

```sh
OPENAI_API_KEY='xxxxxxxxxx'
```

## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
