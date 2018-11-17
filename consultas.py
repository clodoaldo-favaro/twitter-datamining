import pymongo
import configparser
from os.path import isfile
from criptografia import decrypt
from os import remove
from datetime import datetime, timedelta
from email.utils import parsedate_tz
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

glob_tweet_count = 0

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
if not isfile('config.ini'):
    decrypt('config.ini.enc')
config.read('config.ini')
remove('config.ini')
password = config['MONGODB']['password']


# Cria conexao
client = pymongo.MongoClient("mongodb+srv://clodo:" + password + "@orgarq-bcluw.mongodb.net/test?retryWrites=true")

# Acessa a base de dados (ou cria ela)
db = client.tweets

# Recebe o nome do jogo e consulta as datas em que ele foi mencionado
def consulta_frequencia_jogo_por_data(nome_jogo:str):
    resultado = db.tweets_resumidos.find({'text': {'$regex': nome_jogo, '$options': 'i'}}, {'tweet_date':1, '_id':0 })
    frequencia = {}
    for t in resultado:
        #print(t['tweet_date'])
        time_tuple = parsedate_tz(t['tweet_date'].strip())
        chave = str(time_tuple[2]) + '-' + str(time_tuple[1])
        if chave in frequencia:
            frequencia[chave] += 1
        else:
            frequencia[chave] = 1

    for key, value in frequencia.items():
        print(key, '>>>>', value)

    plt.bar(range(len(frequencia)), frequencia.values(), align='center')
    plt.xticks(range(len(frequencia)), list(frequencia.keys()), rotation='vertical', fontsize=6)
    plt.xlabel(nome_jogo, fontsize=12)
    plt.tight_layout()
    plt.plot(figsize=(1024, 768))
    plt.show()









def consulta_nome_jogo(jogo_consulta):
    resultado = db.tweets_resumidos.find({'text': {'$regex': jogo_consulta, '$options': 'i'}})
    return resultado

def consulta_nome_usuario(nome_usuario_consulta):
    resultado = db.tweets_resumidos.find({'user_screen_name': nome_usuario_consulta})
    return resultado

def consulta_id_tweet(tweet_id_consulta):
    resultado = db.tweets_resumidos.find_one({'tweet_id':tweet_id_consulta})
    return resultado


def mostrar_tweet(resultado_pesquisa):
    for tweet in resultado_pesquisa:
        print(tweet['text'])

def mostrar_tweet_unico(tweet):
    print(tweet['text'])



def main():
    opcao = 0
    while True:
        opcao = input('1. CONSULTAR NOME JOGO\n2. CONSULTAR NOME USUARIO\n3. CONSULTAR ID TWEET\n4. MOSTRAR DATAS NOME JOGO\n5. SAIR\n')
        if opcao == '5':
            break
        elif opcao == '1':
            consulta = input('Informe o nome do jogo\t\t')
            resultado = consulta_nome_jogo(consulta)
            mostrar_tweet(resultado)
        elif opcao == '2':
            consulta = input('Informe o nome do usuario\t\t')
            resultado = consulta_nome_usuario(consulta)
            mostrar_tweet(resultado)
        elif opcao == '3':
            consulta = input('Informe o id do tweet\t\t')
            resultado = consulta_id_tweet(consulta)
            mostrar_tweet_unico(resultado)
        elif opcao == '4':
            consulta = input('Informe o nome do jogo\t\t')
            consulta_frequencia_jogo_por_data(consulta)
        else:
            print('Opcao invalida')


if __name__ == '__main__':
    main()










