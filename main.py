import tweepy
import pickle
import os
import operator
import configparser
import tweet
import jsonpickle



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


# Retorna 100 tweets
tweets = tweepy.Cursor(api.search, q="ps4 playstation4 -filter:retweets", rpp=100, result_type='recent',
                       tweet_mode='extended', exclude_replies=True).items(100)


 
id_list = []
lista_tweets = []
requisicoes = 1


# Salva os dados dos tweets, e continua até o usuário interromper
while True:
    
    for t in tweets:
        print(t.id)
        id_list.append(t.id)
        

        # Percorre as hashtags do tweet, adicionando cada uma à lista
        hashtags_list = []
        for hashtag in t.entities['hashtags']:
            hashtags_list.append(hashtag['text'])
            
        # Cria um objeto tweet
        current_tweet = tweet.Tweet(t.id_str, t.full_text, hashtags_list, t.user.id_str)
        
        
        
        # Adiciona o objeto tweet 
        lista_tweets.append(current_tweet)

    
    print('Requisicao: {requisicoes}'.format(requisicoes = requisicoes))
    #opcao = input('Deseja continuar (Y/N)?')
    requisicoes += 1
    #if opcao.upper() == 'N':
    #    break
    
    
    if requisicoes > 10000:
        break
    # Salva o menor id dos tweets (mais antigo)
    max_id = min(id_list)
    # Pega os próximos 100 tweets com id menor que o id mínimo da requisição anterior
    tweets = tweepy.Cursor(api.search, q="ps4 playstation4 -filter:retweets", rpp=100, result_type='recent',
                           tweet_mode='extended', max_id=max_id - 1, exclude_replies=True).items(100)
    
    
    
    

# Serializa os objetos json e salva em um arquivo
with open('tweets.json', 'w', encoding='utf-8') as json_file:
    json_file.write(jsonpickle.encode(lista_tweets))






print('Quantidade de tweets salvos: {qtde_tweets}: '.format(qtde_tweets = len(id_list)))
    

    
    



