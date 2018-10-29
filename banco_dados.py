import pymongo
import json
import configparser
import sys

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



# Cria um dict (documento json) para todos os tweets no arquivo
with open('tweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        if 'extended_tweet' in tweet:
            texto = tweet['extended_tweet']['full_text']
        else:
            texto = tweet['text']
        # Cria um objeto json apenas com as informacoes necessarias
        tweet_resumido = {
            'tweet_id': tweet['id'],
            'text': texto,
            #'tweet_date': tweet['created_at'],
            #'user_id': tweet['user']['id'],
            #'user_screen_name': tweet['user']['screen_name'],
            #'user_name': tweet['user']['name']
        }
        # Só adiciona hashtags se existirem
        lista_hashtags = []
        if tweet['entities']['hashtags']:
            for hashtag in tweet['entities']['hashtags']:
                lista_hashtags.append(hashtag['text'])
            # Adiciona a lista de hashtags ao json
            tweet_resumido['hashtags'] = lista_hashtags

        print('Tamanho do tweet resumido: ', sys.getsizeof(tweet_resumido))

        # Insere um documento em uma colecao
        status_id = tweets_resumidos.insert_one(tweet_resumido).inserted_id
        break





print(db.collection_names(include_system_collections=False))