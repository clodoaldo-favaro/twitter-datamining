import tweepy
import pickle
import os
import operator

# Sobre url de busca no twitter
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
# https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
# https://developer.twitter.com/en/docs


class Tweet():

    def __init__(self, id, text):
        self.id = id
        self.text = text


consumer_key = "====="
consumer_secret = "====="
access_token = "===="
access_token_secret = "==="

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

irrelevantes = ['e', 'ou', 'para', 'em', 'na', 'no', 'lá', 'quando', 'que', 'a', 'o', 'mas', 'mais', 'porque', 'por',
                'me', 'de', 'da', 'do']

id_list = {}

# Retorna 100 tweets
tweets = tweepy.Cursor(api.search, q="ps4 playstation4 -filter:retweets", rpp=100, result_type='recent',
                       tweet_mode='extended', exclude_replies=True).items(10)

# Grava os textos dos tweets em um dict
for tweet in tweets:
    id_list[tweet.id_str] = tweet.full_text
    print('tweet id:', tweet.id_str)
    print('user id:', tweet.user.id_str)
    print('full text:', tweet.full_text)
    print('SHOWING HASHTAGS')
    for hashtag in tweet.entities['hashtags']:
        print(hashtag['text'])
exit()
# Salva o id mais antigo, para que a próxima busca seja a partir dele pra baixo
max_id = min(id_list.keys())

# Loop para pegar tweets mais antigos
i = 1
while True:
    # Pega 100 tweets
    tweets = tweepy.Cursor(api.search, q="ps4 playstation4 -filter:retweets", rpp=100, result_type='recent',
                           tweet_mode='extended', max_id=max_id - 1, exclude_replies=True).items(100)

    # Salva o texto
    for tweet in tweets:
        id_list[tweet.id_str] = tweet.full_text
    # Salva o id do tweet mais antigo
    max_id = min(id_list.keys())
    i += 1
    # 100 + 50 * 100 = 5100 tweets
    if i > 50:
        break

max_id = min(id_list.keys())
print(len(id_list))
print(max_id)

# Salva os tweets em um arquivo texto
with open('tweets.txt', 'w', encoding="utf-8") as file:
    for key, value in id_list.items():
        file.write(key + ',' + value + '\n')
        # print(len(value))
