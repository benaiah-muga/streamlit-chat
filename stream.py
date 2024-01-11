import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the chatbot model
os.environ["GOOGLE_API_KEY"] = 'AIzaSyCVeSJn_85Vf2lyQNSGAn90wP9B0SrK-bw'
llm = ChatGoogleGenerativeAI(model="gemini-pro")

def generate_response(prompt):
    result = llm.invoke(prompt)
    return result.content

def main():
    st.title("Stream Chat Assistant")

    # Set up layout with two columns
    col1, col2 = st.columns([1, 3])  # Use st.columns for layout

    with col1:
        st.markdown("---")  # Visual separator
        st.button("New Chat")
        selected_model = st.selectbox("Select Model", ["llama2", "gpt4", "gemini", "mistral", "Claude", "Upcoming Features"])

    with col2:
        st.markdown("---")  # Visual separator
        st.title("Lets Chat!")

        # Manage conversation history using session state
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        for message in st.session_state.conversation:
            st.text(message)

        # Input field for user prompt
        user_prompt = st.text_area("You:")

        # Submit prompt and display response
        if st.button("Send"):
            response = generate_response(user_prompt)
            st.text(f"Bot: {response}")

            # Update conversation history
            st.session_state.conversation.append(f"You: {user_prompt}")
            st.session_state.conversation.append(f"Bot: {response}")

            # Check for quit commands
            if user_prompt.lower() in ["quit", "exit", "stop"]:
                st.stop()

if __name__ == "__main__":
    main()
