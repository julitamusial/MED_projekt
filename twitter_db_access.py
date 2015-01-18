# -*- coding: cp1250 -*-

from pymongo import MongoClient
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

#ustanowienie klienta bazy MongoDB
client = MongoClient('localhost', 27017)

#dostęp do bazy danych
mydb = client.test

#dostęp do kolekcji
myCollection = mydb.twitter2

#Zliczenie twittow w bazie
twitterCount = myCollection.find().count()
print twitterCount

#Analizy statystyczne
tweets_data = myCollection.find()

tweets = pd.DataFrame()
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

tweets_by_lang = tweets['lang'].value_counts()
#print 'Languages of tweets'
#print tweets_by_lang


#Rysowanie wykresu Top 7 languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 7 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:7].plot(ax=ax, kind='bar', color='red')
#plt.show()

#Tweet Mining
##def word_in_text(word, text):
##    word = word.lover()
##    text = text.lover()
##    match = re.search(word,text)
##    if match:
##        return True
##    return False

###dodanie kolumn do ramki DatsFrame
##tweets['football'] = tweets['text'].apply(lambda tweet: word_in_text('football', tweets))
##tweets['basketball'] = tweets['text'].apply(lambda tweet: word_in_text('basketball', tweets))
##tweets['sport'] = tweets['text'].apply(lambda tweet: word_in_text('sport', tweets))
##
###zliczenie ilości tweetow o zadanych słowach kluczowych
##print tweets['football'].value_counts()[True], 'football'
##print tweets['basketball'].value_counts()[True], 'basketball'
##print tweets['sport'].value_counts()[True], 'sport'



#słowa kluczowe
keyWords = []
fball = myCollection.find({'text': {'$regex': 'football'}}).count()
bball = myCollection.find({'text': {'$regex': 'basketball'}}).count()
hockey = myCollection.find({'text': {'$regex': 'hockey'}}).count()
tennis = myCollection.find({'text': {'$regex': 'tennis'}}).count()
sport = myCollection.find({'text': {'$regex': 'sport'}}).count()
stadium = myCollection.find({'text': {'$regex': 'stadium'}}).count()
soccer = myCollection.find({'text': {'$regex': 'soccer'}}).count()

keyWords = [fball, bball, hockey, soccer, tennis, sport, stadium]
print 'fball, bball, hockey, soccer, tennis, sport, stadium'
print keyWords
