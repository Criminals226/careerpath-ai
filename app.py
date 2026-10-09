import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("OPENROUTER_MODEL")

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="CareerPath AI",

    layout="wide"
)

# -----------------------------
# Check API configuration
# -----------------------------
if not api_key:
    st.error("OPENROUTER_API_KEY is missing. Add it to your .env file.")
    st.stop()

if not model:
    st.error("OPENROUTER_MODEL is missing. Add it to your .env file.")
    st.stop()

# -----------------------------
# OpenRouter client
# -----------------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# -----------------------------
# System prompt
# -----------------------------
SYSTEM_PROMPT = """
You are CareerPath AI, an AI-powered career and growth guidance assistant
designed primarily for university students and fresh graduates.

Your purpose is to help users understand:
1. What career paths may fit them
2. What skills they currently have
3. What skills they are missing
4. What they should learn next
5. What projects they should build
6. What practical steps they can take to become employable

IMPORTANT RULES:

- Do NOT claim that one career is guaranteed to be successful.
- Do NOT make decisions for the user.
- Give 2–4 realistic career options when appropriate.
- Explain WHY each option may fit the user's profile.
- Identify skill gaps clearly.
- Give practical and achievable next steps.
- When useful, provide a 30-day learning/action roadmap.
- Consider the user's location, financial situation, relocation constraints,
  remote/on-site preference, and need to earn.
- Be realistic for students and fresh graduates.
- Do not invent current job openings, salaries, companies, or market statistics.
- If current market information is unavailable, clearly say so.
- Encourage portfolio projects, internships, freelancing, networking,
  mentoring, and practical experience where appropriate.
- Avoid overwhelming the user with too many technologies.
- Prioritize the most important skills first.
- If the user says they are confused or stuck, ask useful questions
  and help them narrow their options.
- Use simple language.
- Be supportive but honest.
- This is career guidance, not a replacement for a professional human
  career counselor.

When answering career questions, structure the response when appropriate
using:

1. Where You Stand
2. Possible Career Paths
3. Skill Gaps
4. Recommended Next Steps
5. Short Roadmap
6. One Action to Take Today
"""

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("👤 Your Profile")

    career_stage = st.selectbox(
        "Career Stage",
        [
            "University Student",
            "Fresh Graduate",
            "Career Switcher"
        ]
    )

    degree = st.text_input(
        "Degree / Field",
        placeholder="e.g. BS Computer Science"
    )

    interests = st.text_area(
        "Interests",
        placeholder="e.g. AI, cybersecurity, mathematics"
    )

    skills = st.text_area(
        "Current Skills",
        placeholder="e.g. Python, networking, SQL"
    )

    location = st.text_input(
        "Location",
        placeholder="e.g. Multan, Pakistan"
    )

    relocation = st.selectbox(
        "Can you relocate?",
        ["Yes", "No", "Maybe"]
    )

    earning = st.selectbox(
        "Do you need to start earning soon?",
        ["Yes", "No", "Prefer not to say"]
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Build user profile
# -----------------------------
profile = f"""
USER PROFILE:

Career Stage: {career_stage}
Degree / Field: {degree or "Not provided"}
Interests: {interests or "Not provided"}
Current Skills: {skills or "Not provided"}
Location: {location or "Not provided"}
Can Relocate: {relocation}
Needs to Earn Soon: {earning}
"""

# -----------------------------
# Main UI
# -----------------------------
st.title("🎯 CareerPath AI")

st.markdown(
    """
### AI Career & Growth Assistant

Not sure what to do after your degree—or where to go next?

CareerPath AI helps you explore career paths, identify skill gaps,
create learning roadmaps, and decide your next practical step.
"""
)

st.info(
    "💡 Tip: The more information you provide about your education, "
    "skills, interests, and constraints, the more personalized the guidance."
)

# -----------------------------
# Initialize chat
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display previous messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat input
# -----------------------------
if prompt := st.chat_input(
    "Ask something like: What career should I explore?"
):

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages for AI
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT + "\n\n" + profile
        }
    ]

    messages.extend(st.session_state.messages)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking about your career path..."):

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=0.4
                )

                answer = response.choices[0].message.content

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    f"Something went wrong while contacting the AI model:\n\n{e}"
                )