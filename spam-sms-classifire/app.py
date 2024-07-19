"""import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

#import pickle
with open('vectorizer.pkl', 'rb') as file:
    tfidf = pickle.load(file)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")"""


import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Example training data
X_train = ["spam message 1", "ham message 1", "spam message 2", "ham message 2"]
y_train = [1, 0, 1, 0]  # 1 for spam, 0 for ham

# Vectorize the training data
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train the MultinomialNB model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Save the vectorizer and the model
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)


# Streamlit app
st.title('Spam SMS Classifier')

# Input text box
input_text = st.text_area("Enter SMS text to classify:")

if st.button('Classify'):
    # Transform the input text using the loaded vectorizer
    vector_input = vectorizer.transform([input_text])

    # Predict using the loaded and fitted model
    result = model.predict(vector_input)[0]

    # Display the result
    if result == 1:
        st.write("This is a Spam message.")
    else:
        st.write("This is a Ham (Non-Spam) message.")