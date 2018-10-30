import pymongo
import json
import configparser


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

contador = 1

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

        print('Tweet gravado', contador, '   nova id: ', result.upserted_id)
        contador += 1



