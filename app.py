import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 2. Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# 3. Streamlit page setup
st.set_page_config(page_title="AI Text Summarizer", page_icon="🧠", layout="centered")

st.title("🧠 AI Text Summarizer Web App")
st.write("Summarize long text using OpenAI GPT model in real-time.")

# 4. Text input
text_input = st.text_area("Enter text to summarize:", height=250)

# 5. Button trigger
if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            try:
                # 6. Call OpenAI API
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful summarizer."},
                        {"role": "user", "content": f"Summarize this text: {text_input}"}
                    ],
                    temperature=0.5,
                    max_tokens=200
                )

                summary = response.choices[0].message.content
                st.success("✅ Summary Generated Successfully!")
                st.subheader("Summary:")
                st.write(summary)

            except Exception as e:
                st.error(f"Error: {e}")