# Task 3 : AI CHATBOT WITH NLP (Python Project)

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : B.UMA MAHESHWAR

*INTERN ID* : CT06DF1320

*DOMAIN NAME* : PYTHON PROGRAMMING

*DURATION* : 6 WEEKS

*MENTOR* : NEELA SANTOSH 

*UNLEASHING INTELLIGENCE THROUGH NLP AND PYTHON*

In Task 3 of my internship, I was challenged to create a fully functional AI chatbot using Natural Language Processing (NLP) techniques. The goal was to allow users to ask natural questions, receive smart answers, and interact with a friendly user interface. The project was built using Python and key libraries like NLTK, Wikipedia API, Scikit-learn, and Streamlit — bringing together local knowledge, web data, and modern UI design.

🧠 How It Was Built
The chatbot has two main brains — a local knowledge base (with custom Q&A) and a Wikipedia-powered dynamic response engine. I started by writing a dictionary of question-answer pairs (qa_pairs), covering common queries like "What is Python?", "Who is Elon Musk?", or "Tell me a joke". These responses are hardcoded and serve as the chatbot’s core knowledge.

To make the chatbot understand language more intelligently, I used the Natural Language Toolkit (NLTK) for tokenization and stopword removal. This helped clean the user’s input by removing unnecessary words like “the”, “is”, “and”, etc. Each question in the knowledge base was processed and vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) via TfidfVectorizer. This allowed the chatbot to compare user input with stored questions using cosine similarity and match it to the closest intent.

However, relying only on hardcoded questions makes any chatbot limited. So I integrated Wikipedia as a dynamic source of information. If a user asked, “Who is Nelson Mandela?” or “Tell me about black hole,” the chatbot fetches a real-time summary from Wikipedia using the wikipedia Python module. This gives the bot a massive range of topics to respond to, without bloating the local knowledge base.

The final touch was creating a clean and friendly GUI using Streamlit — a Python-based web framework. Streamlit’s chat_input and chat_message widgets helped simulate a natural chat interface, complete with scrolling history and two-sided interaction (user & bot). The app has a page title, emoji styling, and remembers chat history using session state.

I have made it with the help of resources from Google, Youtube & Chatgpt. It's great but still has some flaws like not able to recognize some people or places. It was fun to make despite it's flaws. Run the code by typing : python -m streamlit run (filename).py on your terminal. You also need to install the required library - pip install nltk streamlit wikipedia

🌟 Why This Chatbot Matters
This chatbot isn’t just a demo — it’s a lightweight intelligent assistant that combines the best of both worlds: offline NLP logic and online knowledge lookup. It’s fast, works in the browser, and doesn’t rely on large cloud models or API keys. More importantly, it shows how even limited resources (like NLTK and a small script) can be stretched to make a helpful, smart, and engaging chatbot.

🛠️ Applications
📚 Educational assistants: For answering questions in schools, tutorials, or coding platforms

🛒 E-commerce: Product FAQs or customer support bots

🌐 Info kiosks: Travel information, location details, or general queries

💬 Personal assistant: Reminders, facts, jokes, or explanations

💡 Final Thoughts
Through this project, I learned how to combine NLP, information retrieval, and user interface design to build a complete conversational system. From text cleaning and similarity scoring to Wikipedia scraping and Streamlit-based deployment — this task helped me bridge the gap between traditional chatbot logic and modern interactive tools.

It’s a simple yet powerful foundation for smarter AI systems in the future. 🚀

*Output* 

![Image](https://github.com/user-attachments/assets/5c4ebb55-5aef-4bb6-b1c5-f8a8caecd4fc)
![Image](https://github.com/user-attachments/assets/7c33acd1-98f0-4548-bde1-462214f64a7f)
![Image](https://github.com/user-attachments/assets/01ed6139-2393-4425-b08c-27b416b92f15)
![Image](https://github.com/user-attachments/assets/2f0d1026-ac6a-470c-b95e-83d0d91eae7e)

As you can see , sometimes, it does not give the appropriate answer. But most of the time, it works perfectly. 
