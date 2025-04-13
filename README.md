# CLAT Chatbot

This project is a simple rule-based or NLP-powered chatbot that answers CLAT-related queries. It is built using **spaCy** for NLP processing and **Streamlit** for the web interface. The chatbot answers queries like:

- "What is the syllabus for CLAT 2025?"
- "How many questions are there in the English section?"
- "Give me last year’s cut-off for NLSIU Bangalore."

## Features

- **Query-based Responses**: The chatbot accepts user queries and responds with relevant answers based on a predefined knowledge base or FAQs.
- **Streamlit Interface**: The chatbot is deployed as a web app using Streamlit.
- **NLP Model**: Uses spaCy for basic natural language processing to understand and respond to queries.

## Requirements

- Python 3.7+
- Libraries:
  - spaCy
  - Streamlit
  - fuzzywuzzy
  - pandas

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone
cd clat-chatbot
2. Create a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv clat_env
source clat_env/bin/activate   # On Windows: clat_env\Scripts\activate
3. Install Required Dependencies
Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
4. Download spaCy Model
Download the spaCy model en_core_web_sm:

bash
Copy
Edit
python -m spacy download en_core_web_sm
5. Run the Streamlit App
Run the Streamlit app with:

bash
Copy
Edit
streamlit run app.py
This will open a web interface on your browser where you can interact with the chatbot.

Project Structure
bash
Copy
Edit
clat-chatbot/
│
├── app.py               # Streamlit app code
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── data/                # Folder containing knowledge base or data files
Knowledge Base
The chatbot uses a small knowledge base of CLAT-related queries. You can expand or modify this knowledge base by editing the relevant files in the data/ folder or updating the response logic in the app.py file.

How to Use
Open the Streamlit app by navigating to the folder and running streamlit run app.py.

Type your query related to CLAT (e.g., "What is the syllabus for CLAT 2025?").

The chatbot will return a relevant answer based on its training or a keyword-based search.
```
