import tweepy
import configparser
import mylistener

# Sobre url de busca no twitter
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
# https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
# https://developer.twitter.com/en/docs

# Carrega as chaves de acesso
config = configparser.ConfigParser()
config.read('config.ini')

# Salva os dados para acesso
consumer_key = config['CONSUMER KEY']['consumer_key']
consumer_secret = config['CONSUMER KEY']['consumer_secret']
access_token = config['ACCESS TOKEN']['access_token']
access_token_secret = config['ACCESS TOKEN']['access_token_secret']

# Acessa a api do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Define os termos a serem ignorados no processamento dos textos
irrelevantes = ['e', 'ou', 'para', 'em', 'na', 'no', 'lá', 'quando', 'que', 'a', 'o', 'mas', 'mais', 'porque', 'por',
                'me', 'de', 'da', 'do']


# Abrindo a stream
stream_listener = mylistener.Listener()
stream = tweepy.Stream(auth = api.auth, listener = stream_listener, tweet_mode= 'extended')

stream.filter(track=["ps4", "playstation4", "playstation 4"])











