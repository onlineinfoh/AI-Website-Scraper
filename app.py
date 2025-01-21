from bot import scrape,extract,clean,split
from summarize import summarize_with_ollama

import streamlit as st
st.title("Author: Tianxi Liang")

url = st.text_input("Web Scraper: Enter the website URL")

if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")
        result = scrape(url)
        body_content = extract(result)
        cleaned_content = clean(body_content)

        # Store the content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=400)


# Ask Questions About the contents
if "dom_content" in st.session_state:
    description = st.text_area("Describe what you want to summarize")

    if st.button("Summarize Content"):
        if description:
            st.write("Summarize the content...")

            dom_chunks = split(st.session_state.dom_content)
            parsed_result = summarize_with_ollama(dom_chunks, description)
            st.write(parsed_result)