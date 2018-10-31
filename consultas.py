import pymongo
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




jogo_consulta = input('Informe o jogo que deseja procurar:\t\t')

resultado = db.tweets_resumidos.find({'text': {'$regex': jogo_consulta, '$options': 'i'}})

for tweet in resultado:
    print(tweet['text'])




