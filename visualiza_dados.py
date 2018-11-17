import pymongo
import configparser
import pprint
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from wordcloud import WordCloud
from os.path import isfile
from criptografia import decrypt
from os import remove

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
# Descriptografar
if not isfile('config.ini'):
    decrypt('config.ini.enc')
config.read('config.ini')
remove('config.ini')
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


print('1. Gráfico de barras')
print('2. Wordcloud')
opcao = input('Selecione a opcao desejada:\t\t')

if opcao == '1':
    plt.bar(range(len(frequencia_jogo)),frequencia_jogo.values(), align='center')
    plt.xticks(range(len(frequencia_jogo)), list(frequencia_jogo.keys()), rotation='vertical', fontsize=6)
    plt.xlabel('Jogos', fontsize=12)
    plt.tight_layout()
    plt.plot(figsize=(1024, 768))
elif opcao == '2':
    wordcloud = WordCloud(width=1024, height=768).generate_from_frequencies(frequencia_jogo, 100)
    plt.imshow(wordcloud, interpolation='bilinear')

plt.show()
