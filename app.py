import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to solve biology problems
def solve_biology_problem(problem, topic):
    try:
        messages = [
            {"role": "system", "content": f"You are an expert in {topic}."},
            {"role": "user", "content": f"Explain or solve this biology problem step-by-step:\n{problem}"},
        ]
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-4",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# App layout
st.title("Biology Problem Solver")
st.markdown("Ask a biology-related question or describe a problem below.")

topic = st.selectbox("Select a topic", ["Genetics", "Ecology", "Anatomy", "Physiology", "Other"])
problem = st.text_area("Describe your problem or question:")

if st.button("Solve", key="solve_biology_button"):
    solution = solve_biology_problem(problem, topic)
    st.text_area("Solution", solution, height=300)
