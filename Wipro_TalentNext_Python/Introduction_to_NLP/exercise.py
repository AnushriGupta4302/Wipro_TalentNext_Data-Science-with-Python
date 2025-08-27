'''
Ques-1) Perform Text Preprocessing on SMSSpamCollection Dataset.
The dataset can be downloaded from  https://www.kaggle.com/datasets
'''
import pandas as pd
import string
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
              
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
print("Dataset shape:", df.shape)
print(df.head())

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", " ", text)
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)
df["clean_message"] = df["message"].apply(preprocess_text)
print(df[["message", "clean_message"]].head(10))