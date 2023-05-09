import streamlit as st
import openai
import os
import toml


def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]


try:
    # Load API key from secrets.toml
    secrets = toml.load("./.streamlit/secrets.toml")
    openai.api_key = secrets["openai"]["OPENAI_KEY"]

    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text Summarizer")

    input_text = st.text_area(label="Enter full text:", value="", height=250)
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
    output_text = st.text_area(
        label="Summarized text:", value=st.session_state["summary"], height=250)
except:
    st.write('There was an error =(')
