#! /usr/bin/python3
import random
import exmecab
from twihoge import TwitterApi
from markov import Markov
import os
import re

os.chdir(os.path.dirname(__file__))
twitter = TwitterApi.load_json_file('keys.json')

trend = random.choice(twitter.trendwords())
print('trend = ' + trend)

hashtag = ''
hashtagmatch = re.match(r'#.+',trend)
if hashtagmatch is not None:
    hashtag = trend
print('hashtag? = ' + hashtag)

statustexts = twitter.search_statustexts(trend,300)
statustexts = [re.sub(r'RT.+:','',statustext) for statustext in statustexts]
statustexts = [re.sub(hashtag,'',statustext) for statustext in statustexts]
statustexts = [re.sub(r'http.+(\n|\Z)','',statustext) for statustext in statustexts]
print(statustexts)

markov = Markov(2)
for statustext in statustexts:
    markov.learn(exmecab.wakati(statustext))

a_sentence = exmecab.wakati(random.choice(statustexts)).split(' ')
start_words = tuple(a_sentence[:2])

salad = markov.make_salad(50,start_words)
while len(salad) < 20:
    salad = markov.make_salad(50,start_words)

maxlen = 140 - len(hashtag)
if len(salad) > maxlen:
    salad = salad[:maxlen-1]

salad += hashtag
print(salad)
print('len = ' + str(len(salad)))
twitter.tweet(salad)
