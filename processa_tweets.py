import json




with open('tweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        if 'extended_tweet' in tweet:
            texto = tweet['extended_tweet']['full_text']
        else:
            texto = tweet['text']
        termos = texto.split()
        for termo in termos:
            if len(termo) > 3 and termo.istitle():
                print(termo) 

