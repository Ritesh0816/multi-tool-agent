import streamlit as st
from agent import run_agent

st.title("🤖 Multi Tool Agent")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
query = st.chat_input("Ask something")

if query:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    # Run agent
    logs, answer = run_agent(query)

    # (Optional) Print logs in terminal for debugging
    for log in logs:
        print(log)

    # Store ONLY the final answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()