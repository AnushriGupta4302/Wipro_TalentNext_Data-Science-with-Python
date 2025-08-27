#Ques 1 Write a program to find check if a string has only octal digits. Given string ['789', '123', '004"]

strings = ['789', '123', '004']
def is_octal(s):
    return all(ch in '01234567' for ch in s)
for s in strings:
    if is_octal(s):
        print(f"'{s}' contains only octal digits.")
    else:
        print(f"'{s}' does not contain only octal digits.")

'''Ques 2 Extract the user id, domain name and suffix from the following email addresses.
emails = """zuck@facebook.com 
sunder33@google.com 
jeff42@amazon.com"""
'''

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
email_list = emails.splitlines()
for email in email_list:
    user, domain = email.split('@')
    domain_name, suffix = domain.split('.')
    print(f"User ID: {user}, Domain: {domain_name}, Suffix: {suffix}")


'''Ques 3 Split the following irregular sentence into proper words 
sentence ='''A, very  very; irregular_sentence''' ## expected output: A very very irregular sentence
'''

import re

sentence = '''A, very  very; irregular_sentence'''
words = re.sub(r'[^a-zA-Z]', ' ', sentence)
clean_sentence = ' '.join(words.split())
print(clean_sentence)


''' Ques 4 Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0px0d cc: @garybernhardt #rstats'''
##desired_output = 'Good advice What I would do differently if I was learning to code today'
'''

import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0px0d cc: @garybernhardt #rstats'''
tweet = re.sub(r'\brt\b', '', tweet, flags=re.IGNORECASE)
tweet = re.sub(r'\bcc\b', '', tweet, flags=re.IGNORECASE)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'[^\w\s]', '', tweet)
clean_tweet = ' '.join(tweet.split())
print(clean_tweet)


''' Ques 5
Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html

Code to retrieve the HTML page is given below:

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here

desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 
                  'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
'''

import requests
from bs4 import BeautifulSoup
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
soup = BeautifulSoup(r.text, 'html.parser')
texts = [t.strip() for t in soup.find_all(string=True) if t.strip()]
print(texts)

''' Ques 6 Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as
''' 
words = ["civic","trust","widows","maximum","museums","aa","as"]
same_ends = [w for w in words if w[0] == w[-1]]
print(same_ends)