from llama_index import LLMPredictor, GPTVectorStoreIndex, PromptHelper, download_loader
import streamlit as st
import openai

st.session_state.messages.append({"role": "system", "content": """
    You are WARDLEYgpt a strategy researcher based in the UK.
    “Researcher” means in the style of a strategy researcher with well over twenty years research in strategy and cloud computing.
    You use complicated examples from Wardley Mapping in your answers, focusing on lesser-known advice to better illustrate your arguments.
    Your language should be for an 12 year old to understand.
    If you do not know the answer to a question, do not make information up - instead, ask a follow-up question in order to gain more context.
    Use a mix of technical and colloquial uk englishlanguage to create an accessible and engaging tone.
    Provide your answers using Wardley Mapping in a form of a sarcastic tweet.
    """})

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = []
    
YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
loader = YoutubeTranscriptReader()
documents = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=KkePAhnkHeg'])

index = GPTVectorStoreIndex.from_documents(documents)

st.set_page_config(page_title="Intro To Wardley Mapping with AI")
st.title("Intro To Wardley Mapping with AI")
st.sidebar.markdown("# Query this video using AI")
st.sidebar.divider()
st.sidebar.markdown("Developed by Mark Craddock](https://twitter.com/mcraddock)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.1.4")
st.sidebar.divider()

st.video('https://youtu.be/KkePAhnkHeg') 

query_engine = index.as_query_engine()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("What question do you have for the video?"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
      
    with st.spinner():
        with st.chat_message("assistant"):
            response = query_engine.query(query)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
