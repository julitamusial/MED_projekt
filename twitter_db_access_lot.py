# -*- coding: cp1250 -*-

from pymongo import MongoClient
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

#ustanowienie klienta bazy MongoDB
client = MongoClient('localhost', 27017)

#dostęp do bazy danych
mydb = client.twitter_lot

#dostęp do kolekcji
myCollection = mydb.lotWszystkieKW

#Zliczenie twittow w bazie
twitterCount = myCollection.find().count()
print twitterCount

#Analizy statystyczne
tweets_data = myCollection.find()

tweets = pd.DataFrame()
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)

tweets_by_lang = tweets['lang'].value_counts()
print 'Languages of tweets'
print tweets_by_lang


#Rysowanie wykresu Top languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top languages', fontsize=15, fontweight='bold')
tweets_by_lang[:7].plot(ax=ax, kind='bar', color='red')
plt.show()

#słowa kluczowe
keyWordsCount = []
lotDict = []
airport = myCollection.find({'text': {'$regex': 'airport', '$options': 'i'}}).count()
plane =myCollection.find({'text': {'$regex': 'plane', '$options': 'i'}}).count()
flight =myCollection.find({'text': {'$regex': 'flight', '$options': 'i'}}).count()

keyWordsCount = [airport, plane, flight]
print 'airport, plane, flight'
print keyWordsCount

#dodaje kolekcję do tablicy
keyWords = []
for item in myCollection.find():
    keyWords.append(item)
print 'keyWords:', len(keyWords)

#zapisuje wspolrzędne do pliku txt
keyWords2 = []
lotFile = open('lotniskaWsp_OK.txt', 'w')
for i in range(0, len(keyWords)):
    keyWords2 = str(keyWords[i]['geo']['coordinates']) + '\n'
    print keyWords2
    lotFile.writelines(keyWords2)
print 'keyWords2:', len(keyWords2)
lotFile.close()


client.disconnect()
