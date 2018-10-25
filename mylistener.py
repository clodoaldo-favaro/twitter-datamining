import tweepy
import json

class Listener(tweepy.StreamListener):

    """
    # Sobrescrever método. on_data = o que vai fazer com os dados? No nosso caso: mostrar o texto e salvar
    def on_data(self, raw_data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(raw_data)
                json_data = json.loads(raw_data)
                print(json_data['text'])
                print(type(json_data))
                return True
        except BaseException as e:
            print('Error on_data: {error_message}'.format(error_message = e))
        return True
    """


    def on_status(self, status):

        try:
            with open('tweets.json', 'a') as f:

                if (not status._json['retweeted']) and (not status._json['text'].startswith('RT @')):
                    #print(status)
                    data = json.dumps(status._json)
                    if 'extended_tweet' in status._json:
                        print('TWEET GRANDE')
                        print(len(status._json['extended_tweet']['full_text']))
                        print(status._json['extended_tweet']['full_text'])
                    f.write(data + '\n')



        except BaseException as e:
            print('Error on_data: {error_message}'.format(error_message=e))
        return True





    def on_error(self, status_code):
        print(status_code)
        return True

