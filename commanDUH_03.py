from gensim import corpora, models, similarities
from nltk.tokenize import word_tokenize
import numpy as np
from numpy import dot
from numpy.linalg import norm
import csv
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are available
import nltk
nltk.download('punkt')

# Load the CSV file
docs = []
with open('crowley.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        docs.append({'title': row['title'], 'text': row['text']})

# Tokenize the documents
texts = [word_tokenize(doc['text'].lower()) for doc in docs]

# Train the Word2Vec model
w2v_model = Word2Vec(sentences=texts, vector_size=100, window=5, min_count=1, workers=4)

def cosine_similarity(vec1, vec2):
    denom = (norm(vec1) * norm(vec2))
    if denom == 0:
        return 0  # Return a similarity of 0 if either vector has zero length
    else:
        return dot(vec1, vec2) / denom


# Function to get the mean vector for a list of words using a trained Word2Vec model
def get_mean_vector(word2vec_model, words):
    words = [word for word in words if word in word2vec_model.wv]
    if len(words) >= 1:
        return np.mean(word2vec_model.wv[words], axis=0)
    else:
        return np.zeros(word2vec_model.vector_size)

# Function to retrieve relevant documents based on cosine similarity
def retrieve_relevant_docs(query, topn=2):
    query_tokens = word_tokenize(query.lower())
    query_vec = get_mean_vector(w2v_model, query_tokens)
    
    doc_vectors = [get_mean_vector(w2v_model, doc) for doc in texts]
    sims = [cosine_similarity(query_vec, doc_vec) for doc_vec in doc_vectors]
    
    sorted_indexes = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)
    relevant_docs = [docs[i] for i in sorted_indexes[:topn]]
    return relevant_docs

# Conversation loop
while True:
    query = input("User: ")
    if query.lower() == "exit":
        break

    relevant_docs = retrieve_relevant_docs(query)

    # Initialize the system prompt with user query included in the preamble for context
    system_prompt = f"""<BOS_TOKEN># Safety Preamble

The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral.

# System Preamble

## Basic Rules

You are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what
kind of response to generate. When you answer the user's requests, you cite your sources in your answers, according to those instructions.

# User Preamble

## Task and Context

You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide

Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.

Query: {query}

<results>
"""

    # Append information about retrieved documents to the system prompt
    for i, doc in enumerate(relevant_docs):
        system_prompt += f"\nDocument {i}: Title: {doc['title']}, Text: {doc['text'][:50]}...\n"

    system_prompt += """</results>

Carefully perform the following instructions, in order, starting each with a new line.

Firstly, Decide which of the retrieved documents are relevant to the user's last input by writing 'Relevant Documents:' followed by comma-separated list of document numbers. If none are relevant, you should instead write 'None'.

Secondly, Decide which of the retrieved documents contain facts that should be cited in a good answer to the user's last input by writing 'Cited Documents:' followed a comma-separated list of document numbers. If you dont want to cite any of them, you should instead write 'None'.

Thirdly, Write 'Answer:' followed by a response to the user's last input in high quality natural english. Use the retrieved documents to help you. Do not insert any citations or grounding markup.

Finally, Write 'Grounded answer:' followed by a response to the user's last input in high quality natural english. Use the symbols <co: doc> and </co: doc> to indicate when a fact comes from a document in the search result, e.g <co: 0>my fact</co: 0> for a fact from document 0.
"""

    print(system_prompt)
    # Here, you can add code to send the system_prompt to an AI model and get a response
    # Then, you can print or process the response as needed

print("Conversation ended.")
