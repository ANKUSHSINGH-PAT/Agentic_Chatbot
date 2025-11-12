import streamlit as st
from langchain_groq import ChatGroq
import os


class GroqLLM:
    def __init__(self, user_controls_input: dict):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
        groq_model = self.user_controls_input.get("selected_groq_model")
        if not groq_api_key or os.getenv("GROQ_API_KEY")=="":
            st.error("GROQ API key or model is missing.")
            return None
        try:
            return ChatGroq(api_key=groq_api_key,model=groq_model)
        except Exception as e:
            st.error(f"Error initializing GROQ LLM: {e}")
            return None
