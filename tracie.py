import streamlit as st
from streamlit import sidebar
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
from dotenv import load_dotenv
import os
import io

# Load your environment variables if needed
load_dotenv()

#api_key = os.getenv("API_KEY")
st.title(' :blue[Tracie 💬]')
#st.title("Tracie 💬")
#st.title(' :orange[Tracie]:winking face with tongue:')


font_css = """
<style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;
    }
    .st-bf {
        font-size: 40px;
        margin-bottom: 20px;
    }
    .st-b6 {  /* Add this for specific styling of the sidebar header */
        font-size: 20px;  /* Adjust as needed */
        text-align: center;  /* Optional: Center align the text */
    }
</style>
"""
st.markdown(font_css, unsafe_allow_html=True)

gemini_pro, llama_2, WEb_chat = st.tabs(["Gemini Pro", "llama 2", "Chat with Any website"])

def interact_with_llama2(messages):
    client = OpenAI(
    api_key=os.getenv("LLAMA2_API_KEY"),  
    base_url="https://api.llama-api.com"
)

    response = client.chat.completions.create(
    model="llama-70b-chat",
    messages=messages
    )

    return response.choices[0].message.content

def main():
    from streamlit import sidebar

    # Sidebar header
    sidebar_css = """
    <style>
        .stApp .sidebar {
            background-color: black;  /* Change to desired grey shade */
            padding: 10px;
            color: white;
        }
        .stApp .sidebar button {
            background-color: white;
            border-color: #EEEEEE;
            color: #333333;
            padding: 5px 10px;
            width: 100%;
        }
    </style>
    """
    st.markdown(sidebar_css, unsafe_allow_html=True)
   
    with sidebar:
        st.header("Lets chat 😜")
        # Buttons
        new_chat_button = st.button("New Chat", use_container_width=True)
        chat_history_button = st.button("Chat History", use_container_width=True)
        analyze_pdf_button = st.button("Analyse PDF", use_container_width=True)

        # Content area below buttons (replace with your actual content)

        # st.write("""Expand your knowledge and understanding of the 
        #          world around you? By having access to a wealth of 
        #          resources, from articles and videos to interactive 
        #          quizzes and games. Learning new things, exploring different 
        #          perspectives""", )
        st.write('<p style="font-family: DM Sans; font color: white font-size: 18px; background-color: #565bbb; ">Expand your knowledge and understanding of the world around you? By having access to a wealth of resources, from articles and videos to interactive quizzes and games. Learning new things, exploring different perspectives</p>', unsafe_allow_html=True)

        
    with gemini_pro:
        st.write("")
        prompt = st.text_input("Ask Me Anything", placeholder="Enter your prompt here...", label_visibility="visible", key="gemini")
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GEMINI_API_KEY"), stream=True)

        
        if st.button("SEND", use_container_width=True):
            result = llm.invoke(prompt)

            st.write("")
            st.header(":blue[Response]")
            st.write("")
            st.markdown(result.content)

    with llama_2:
        st.write("")
        llama2_prompt = st.text_input("Ask Me Anything", placeholder="Enter your prompt here...", label_visibility="visible", key="llama 2", value=prompt)

        
        if st.button("SEND to Llama2", use_container_width=True):
            llama2_messages = [{"role": "user", "content": llama2_prompt}]
            llama2_response = interact_with_llama2(llama2_messages)

            st.write("")
            st.header(":orange[Response from Llama2]")
            st.write("")
            st.markdown(llama2_response)

if __name__ == "__main__":
    main()
