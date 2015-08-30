import os
import random
import MeCab
from twihoge import TwitterApi
from markov import Markov

os.chdir(os.path.dirname(__file__))
twitter = TwitterApi.load_json_file('keys.json')

trend = random.choice(twitter.trendwords())
statustexts = twitter.search_statustexts(trend,100)
text = ''
for status in statustexts:
    text += status

tagger = MeCab.Tagger('-O wakati')
sentence = tagger.parse(text).rstrip('\n').split(' ')

Markov(sentence,2)

print(Markov.create())
