from twihoge import TwitterApi

twitter = TwitterApi.load_json_file('keys.json')
print(twitter.trendwords())
