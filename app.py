import streamlit as st
import joblib

# Function to load the machine learning model
@st.cache(allow_output_mutation=True)
def load_model():
    # Replace 'your_model.pkl' with the path to your model file
    return joblib.load('your_model.pkl')

# Load your machine learning model
model = load_model()

# Function to generate a response from your model
def generate_model_response(user_input):
    # If your model expects a specific format or preprocessing, adjust accordingly
    return model.predict([user_input])[0]

# Function to display the chat history
def display_chat():
    if 'chat_history' in st.session_state:
        for sender, message in st.session_state.chat_history:
            st.text(f'{sender}: {message}')

# Function to send messages
def send_message():
    user_message = st.session_state.user_input
    if user_message:
        st.session_state.chat_history.append(('You', user_message))
        bot_response = generate_model_response(user_message)
        st.session_state.chat_history.append(('Chatbot', bot_response))
        st.session_state.user_input = ''

# Function to clear the chat history
def clear_chat():
    st.session_state.chat_history = []

# Main function to render the Streamlit app
def main():
    st.title("Connected Systems Institute - Chatbot")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    display_chat()

    # Message input
    user_input = st.text_input("Type your message here...", value=st.session_state.user_input, key="user_input", on_change=send_message)
    if st.button("Send"):
        send_message()

    # Sidebar for additional actions
    with st.sidebar:
        st.markdown('This is CSI Chatbot which will assist in answering any questions related to the test bed.')
        if st.button('Clear Chat'):
            clear_chat()

if __name__ == "__main__":
    main()
