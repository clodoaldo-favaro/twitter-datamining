import pymongo
import configparser

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
config.read('config.ini')
password = config['MONGODB']['password']


# Cria conexao
client = pymongo.MongoClient("mongodb+srv://clodo:" + password + "@orgarq-bcluw.mongodb.net/test?retryWrites=true")

# Acessa a base de dados (ou cria ela)
db = client.tweets

result = db.tweets_resumidos.create_index([('tweet_id', pymongo.ASCENDING)], unique=True)

for item in sorted(db.tweets_resumidos.index_information()):
    print(item)