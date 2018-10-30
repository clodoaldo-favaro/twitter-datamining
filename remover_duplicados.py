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


pipeline = [{'$group': {'_id': '$tweet_id', 'count': {'$sum': 1}, 'ids': {'$push': '$_id'}}},
    {'$match': {'count': {'$gte': 2}}}]


bulk = db.tweets_resumidos.initialize_ordered_bulk_op()
requests = []
for document in db.tweets_resumidos.aggregate(pipeline):
    it = iter(document['ids'])
    next(it)
    for id in it:
        requests.append(pymongo.DeleteOne({'_id': id}))

db.tweets_resumidos.bulk_write(requests)


