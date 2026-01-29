import os
import openai

# Set API key from Streamlit secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("🚨 AI Manipulation Detector 🚨")
st.write("Paste text below and watch it get brutally analyzed!")

# Text input
user_input = st.text_area("Enter text here:")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Paste some text first!")
    else:
        prompt = f"""
Analyze the following text for psychological manipulation.
Identify persuasion techniques, emotional triggers, power dynamics, and hidden intent.
Be concise, direct, and ruthless.
Output in bullet points and give a final 'Manipulation Score' out of 10.

Text:
{user_input}
        """
        with st.spinner("Analyzing..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=300
            )
        result = response['choices'][0]['message']['content']
        st.markdown(f"**Analysis:**\n\n{result}")
