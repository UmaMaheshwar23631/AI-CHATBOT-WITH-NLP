import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia
import numpy as np

# Stopwords
stop_words = set(stopwords.words('english'))

# Local QA knowledge base
qa_pairs = {
    "hello": "Hello there! How can I assist you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm a smart chatbot built with NLTK!",
    "what is python": "Python is a powerful, high-level programming language used for AI, web, data, and more.",
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "what is machine learning": "Machine learning is a field of AI that enables computers to learn from data.",
    "who is the prime minister of india": "As of now, the Prime Minister of India is Narendra Modi.",
    "what is the capital of france": "The capital of France is Paris.",
    "what is 2 + 2": "2 + 2 equals 4.",
    "what is the square root of 16": "The square root of 16 is 4.",
    "tell me a joke": "Why did the developer go broke? Because he used up all his cache!",
    "who is albert einstein": "Albert Einstein was a theoretical physicist known for the theory of relativity.",
    "what is gravity": "Gravity is a force that attracts two bodies towards each other.",
    "what is blockchain": "Blockchain is a decentralized digital ledger used in cryptocurrencies like Bitcoin.",
    "what is the internet": "The Internet is a global network that connects millions of computers worldwide.",
    "what is a chatbot": "A chatbot is a software application used to conduct online conversations.",
    "what is cloud computing": "Cloud computing allows access to computing resources over the internet.",
    "what is 5 multiplied by 7": "5 multiplied by 7 is 35.",
    "what is the largest planet": "The largest planet in our solar system is Jupiter.",
    "who is elon musk": "Elon Musk is the CEO of Tesla and SpaceX.",
    "thank you": "You're very welcome!",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a nice day 😊",
    "who created you": "I was created using Python, NLTK, and some intelligent programming!",
    "what can you do": "I can answer your questions, tell jokes, and simulate basic conversation.",
    "do you like humans": "I do! You're fascinating and creative beings.",
    "can you learn": "Right now I can't learn like ChatGPT, but I'm getting better every day!",
    "who invented computer": "Charles Babbage is considered the father of the computer.",
    "what is programming": "Programming is the process of writing instructions for computers to perform tasks.",
    "what is data science": "Data science involves analyzing data to extract knowledge and insights.",
    "what is covid-19": "COVID-19 is a disease caused by the SARS-CoV-2 virus.",
    "who is mahatma gandhi": "Mahatma Gandhi was a leader of Indian independence and a symbol of non-violence.",
    "what is democracy": "Democracy is a system of government where citizens exercise power by voting.",
    "who was the first president of india": "Dr. Rajendra Prasad was the first President of India.",
    "how many continents are there": "There are seven continents on Earth.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain above sea level.",
    "who is the richest person": "As of 2025, it's likely Elon Musk or Jeff Bezos, depending on market values.",
    "what is the fastest animal": "The cheetah is the fastest land animal.",
    "how does a computer work": "A computer processes data using hardware and software through input, processing, and output.",
    "can you tell me a fact": "Sure! Honey never spoils. Archaeologists found 3000-year-old honey in Egyptian tombs that was still edible.",
    "how old are you": "I'm just a few lines of Python code, so pretty young!",
    "are you intelligent": "I'm smart enough to chat with you 😄",
}

# Preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    return " ".join([t for t in tokens if t.isalpha() and t not in stop_words])

questions = list(qa_pairs.keys())
answers = list(qa_pairs.values())
processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# Wikipedia logic
def answer_from_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "I tried searching, but I couldn't find any useful info."

# Final response logic
def get_response(user_input):
    clean = user_input.lower()
    
    # Dynamic question handler
    if clean.startswith("who is ") or clean.startswith("tell me about "):
        topic = clean.replace("who is", "").replace("tell me about", "").strip()
        return answer_from_wikipedia(topic)
    
    # Check local responses
    user_clean = preprocess(user_input)
    user_vec = vectorizer.transform([user_clean])
    sim = cosine_similarity(user_vec, X)
    match_index = np.argmax(sim)

    if sim[0][match_index] > 0.3:
        return answers[match_index]
    else:
        return "Hmm... I don’t know that yet, but you can ask me about people, places or topics!"

# Streamlit UI
st.set_page_config(page_title="Intelligent Chatbot", page_icon="🤖")
st.title("🤖 Smart Chatbot (NLTK + Wikipedia)")

if "chat" not in st.session_state:
    st.session_state.chat = []

# Show history
for entry in st.session_state.chat:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

# Chat input
if user_input := st.chat_input("Ask me anything..."):
    st.session_state.chat.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)
    st.session_state.chat.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
