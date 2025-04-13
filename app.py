import streamlit as st
import json
import spacy
from fuzzywuzzy import process

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# Simple intent map using keywords
intent_map = {
    "syllabus": ["syllabus", "subjects", "topics", "portions"],
    "english_questions": ["english", "language", "english section", "questions in english"],
    "cutoff_nlsiu": ["cut off", "nlsiu", "bangalore", "last year's cutoff", "rank"]
}

def detect_intent(query):
    doc = nlp(query.lower())
    tokens = [token.text for token in doc]
    detected = None
    highest_score = 0

    for intent, keywords in intent_map.items():
        match, score = process.extractOne(" ".join(tokens), keywords)
        if score > highest_score and score > 60:  # fuzzy threshold
            detected = intent
            highest_score = score
    return detected

def get_response(intent):
    if intent and intent in knowledge_base:
        return knowledge_base[intent]
    return "Sorry, I couldn't find relevant information for that query."

# Streamlit UI
st.title("📚 CLAT Legal Exam Chatbot")
st.markdown("Ask me anything about CLAT 2025!")

user_input = st.text_input("Enter your query")

if user_input:
    intent = detect_intent(user_input)
    response = get_response(intent)
    st.write("🤖", response)
