import tweepy
import configparser
import mylistener
from criptografia import encrypt, decrypt
from os.path import isfile
from os import remove

# Sobre url de busca no twitter
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
# https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
# https://developer.twitter.com/en/docs




if __name__ == '__main__':


    # Carrega as chaves de acesso
    config = configparser.ConfigParser()
    # Descriptografa o arquivo
    if not isfile('config.ini'):
        decrypt('config.ini.enc')
    config.read('config.ini')
    remove('config.ini')

    # Salva os dados para acesso
    consumer_key = config['CONSUMER KEY']['consumer_key']
    consumer_secret = config['CONSUMER KEY']['consumer_secret']
    access_token = config['ACCESS TOKEN']['access_token']
    access_token_secret = config['ACCESS TOKEN']['access_token_secret']

    # Autentica
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Cria objeto para baixar dados do Twitter
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    # Cria um listener
    stream_listener = mylistener.Listener()
    # Cria um objeto Stream
    stream = tweepy.Stream(auth = api.auth, listener = stream_listener, tweet_mode= 'extended')
    # Começa o stream
    stream.filter(track=["ps4", "playstation4", "playstation 4"],  stall_warnings=True)












