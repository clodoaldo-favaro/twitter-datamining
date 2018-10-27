import tweepy
import json
import sys
glob_tweet_count = 0
class Listener(tweepy.StreamListener):

    def on_status(self, status):

        try:
            with open('tweets.json', 'a') as f:
                if (not status._json['retweeted']) and (not status._json['text'].startswith('RT @')):
                    global glob_tweet_count
                    glob_tweet_count += 1
                    data = json.dumps(status._json)
                    f.write(data + '\n')
                    print("Tweet: {}".format(glob_tweet_count))
                    print(sys.getsizeof(status._json))
        except BaseException as e:
            print('Error on_data: {error_message}'.format(error_message=e))

        return True


    def on_error(self, status_code):
        print(status_code)
        return True

