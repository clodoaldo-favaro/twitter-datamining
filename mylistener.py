import tweepy
import pymongo
import json
import configparser

glob_tweet_count = 0

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
config.read('config.ini')
password = config['MONGODB']['password']


# Cria conexao
client = pymongo.MongoClient("mongodb+srv://clodo:" + password + "@orgarq-bcluw.mongodb.net/test?retryWrites=true")

# Acessa a base de dados (ou cria ela)
db = client.tweets

# Cria uma collection (ou acessa uma)
tweets_resumidos = db.tweets_resumidos



class Listener(tweepy.StreamListener):



    def on_status(self, status):
        if (not 'retweeted_status' in status._json) and (not status._json['text'].startswith('RT')):
            self.salvar_tweet_banco(status._json)



    def salvar_tweet_banco(self, tweet):
        global glob_tweet_count

        if 'extended_tweet' in tweet:
            texto = tweet['extended_tweet']['full_text']
        else:
            texto = tweet['text']
        # Cria um objeto json apenas com as informacoes necessarias
        tweet_resumido = {
            'tweet_id': tweet['id_str'],
            'text': texto,
            'tweet_date': tweet['created_at'],
            'user_id': tweet['user']['id'],
            'user_screen_name': tweet['user']['screen_name'],
            'user_name': tweet['user']['name'],
            'user_location':tweet['user']['location']
        }
        # Só adiciona hashtags se existirem
        lista_hashtags = []
        if tweet['entities']['hashtags']:
            for hashtag in tweet['entities']['hashtags']:
                lista_hashtags.append(hashtag['text'])
            # Adiciona a lista de hashtags ao json
            tweet_resumido['hashtags'] = lista_hashtags


        # Insere um documento em uma colecao
        result = tweets_resumidos.update_one({'tweet_id': tweet_resumido['tweet_id']}, {'$set':tweet_resumido}, upsert=True)

        glob_tweet_count += 1
        print('Tweets gravados:', glob_tweet_count, 'id:', result.upserted_id, 'tweet_id:', tweet_resumido['tweet_id'])




    def on_error(self, status_code):
        if status_code == 420:
            return False


