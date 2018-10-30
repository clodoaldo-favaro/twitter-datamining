import pymongo
import configparser
import pprint
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

glob_tweet_count = 0

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
config.read('config.ini')
password = config['MONGODB']['password']


# Cria conexao
client = pymongo.MongoClient("mongodb+srv://clodo:" + password + "@orgarq-bcluw.mongodb.net/test?retryWrites=true")

# Acessa a base de dados (ou cria ela)
db = client.tweets




lista_jogos = ['WITCHER 3', 'METAL GEAR SOLID V', 'RED DEAD REDEMPTION 2', 'SPIDER-MAN', 'SHADOW OF THE TOMB RAIDER',
               'GOD OF WAR', 'FORTNITE', 'GTA V', 'FIFA 19', 'HORIZON ZERO DAWN', "ASSASSIN'S CREED ODYSSEY", 'SOUL CALIBUR VI',
               'CALL OF DUTY: BLACK OPS 4', 'PES 2019', 'MADDEN NFL 19', 'DETROIT: BECOME HUMAN',
               'FALLOUT SHELTER', "ASSASSIN'S CREED BROTHERHOOD", 'THE ELDER SCROLLS ONLINE']



frequencia_jogo = {}
for jogo in lista_jogos:
    frequencia_jogo[jogo] = db.tweets_resumidos.count_documents({'text': {'$regex': jogo, '$options': 'i'}})

pprint.pprint(frequencia_jogo)

plt.bar(range(len(frequencia_jogo)),frequencia_jogo.values(), align='center')
plt.xticks(range(len(frequencia_jogo)), list(frequencia_jogo.keys()), rotation='vertical', fontsize=6)
plt.xlabel('Jogos', fontsize=12)

#plt.tight_layout()
plt.plot(figsize=(1024, 768))
plt.show()