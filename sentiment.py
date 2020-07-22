from newspaper import Article
from textblob import TextBlob

import nltk
from gtts import gTTS

article = Article('https://www.thebalancecareers.com/what-is-github-and-why-should-i-use-it-2071946')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

mytext = article.summary

print(mytext)


object = TextBlob(mytext)

sentiment = object.sentiment.polarity
print(sentiment)

if sentiment == 0:
    print('the text is neutral')
elif  sentiment > 0:
    print('the text is positive')
else:
    print('the text is negative')




