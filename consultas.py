import pymongo
import configparser
from os.path import isfile
from criptografia import encrypt, decrypt

glob_tweet_count = 0

# Carrega senha para acesso ao banco de dados
config = configparser.ConfigParser()
if not isfile('config.ini'):
    decrypt('config.ini.enc')
config.read('config.ini')
password = config['MONGODB']['password']


# Cria conexao
client = pymongo.MongoClient("mongodb+srv://clodo:" + password + "@orgarq-bcluw.mongodb.net/test?retryWrites=true")

# Acessa a base de dados (ou cria ela)
db = client.tweets


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
        opcao = input('1. CONSULTAR NOME JOGO\n2. CONSULTAR NOME USUARIO\n3. CONSULTAR ID TWEET\n4. SAIR\n')
        if opcao == '4':
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
        else:
            print('Opcao invalida')


if __name__ == '__main__':
    main()










