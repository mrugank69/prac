#Write a program for pre-processing of a text document stop word removal.

import nltk
from nitk.corpus import stopwords
nltk.download ('stopwords')
nltk.download ('punkt')

from nltk.tokenize import word_tokenize
print (stopwords.words ('english'))

sample_text= "oh man, this is pretty cool. We will do more such things"
text_tokens = word_tokenize (sample_text)

tokens_without_sw =[word for word in text_tokens if not word in stopwords.words ('english')]

print (text_tokens)
print (tokens_without_sw)

