import random
import exmecab
from twihoge import TwitterApi
from markov import Markov
import os

os.chdir(os.path.dirname(__file__))
twitter = TwitterApi.load_json_file('keys.json')

trend = random.choice(twitter.trendwords())
statustexts = twitter.search_statustexts(trend,300)

markov = Markov(2)
for statustext in statustexts:
    markov.learn(exmecab.wakati(statustext))

salad = markov.make_salad(50)
while len(salad) < 20:
  salad = markov.make_salad(50)
if len(salad) > 140:
    salad = salad[:139]

twitter.tweet(salad)
