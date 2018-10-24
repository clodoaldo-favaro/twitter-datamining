import tweepy
import pickle
import os
import operator
import configparser
import json

# Sobre url de busca no twitter
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
# https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
# https://developer.twitter.com/en/docs



# Carrega as chaves de acesso
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['CONSUMER KEY']['consumer_key']
consumer_secret = config['CONSUMER KEY']['consumer_secret']
access_token = config['ACCESS TOKEN']['access_token']
access_token_secret = config['ACCESS TOKEN']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

irrelevantes = ['e', 'ou', 'para', 'em', 'na', 'no', 'lá', 'quando', 'que', 'a', 'o', 'mas', 'mais', 'porque', 'por',
                'me', 'de', 'da', 'do']

id_list = {}

# Retorna 100 tweets
tweets = tweepy.Cursor(api.search, q="ps4 playstation4 -filter:retweets", rpp=100, result_type='recent',
                       tweet_mode='extended', exclude_replies=True).items(3)

# Grava cada tweet em uma lista de json
lista_tweets = []
tweet_json = {}
for tweet in tweets:
    id_list[tweet.id_str] = tweet.full_text
    tweet_json['tweet_id'] = tweet.id_str
    tweet_json['user_id'] = tweet.user.id_str
    tweet_json['text'] = tweet.full_text

    # Percorre as hashtags do tweet, adicionando cada uma à lista
    hashtags_list = []
    for hashtag in tweet.entities['hashtags']:
        hashtags_list.append(hashtag['text'])
    # Adiciona a lista no dict tweet_json
    tweet_json['hashtags'] = hashtags_list
    # Adiciona o tweet_json à lista de objetos json
    lista_tweets.append(tweet_json)

lista_json = {"tweets": lista_tweets}

# Serializa os objetos json e salva em um arquivo
with open('tweets.json', 'w+') as json_file:
    json.dump(lista_json, json_file)



exit()


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
