import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

text = st.text_area("Enter Text")

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    st.write("Translated Text:")
    st.success(translated)