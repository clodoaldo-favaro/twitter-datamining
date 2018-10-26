import tweepy
import json

class Listener(tweepy.StreamListener):

    def on_status(self, status):

        try:
            with open('tweets.json', 'a') as f:
                if (not status._json['retweeted']) and (not status._json['text'].startswith('RT @')):
                    data = json.dumps(status._json)
                    f.write(data + '\n')
        except BaseException as e:
            print('Error on_data: {error_message}'.format(error_message=e))

        return True


    def on_error(self, status_code):
        print(status_code)
        return True

