import streamlit as st
from openai import OpenAI

# Load the OpenAI API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Cadastral Proposal Drafting Assistant")

query = st.text_area("Describe the property situation or survey details you want help drafting:")

if st.button("Generate Proposal"):
    if query.strip():
        with st.spinner("Generating proposal..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant experienced in cadastral surveying in Victoria, Australia."},
                    {"role": "user", "content": query}
                ],
                temperature=0.5
            )
            st.success("Draft generated:")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter some details to generate a proposal.")
