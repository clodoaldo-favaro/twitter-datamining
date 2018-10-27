import tweepy
import json


glob_tweet_count = 0


class Listener(tweepy.StreamListener):



    def on_status(self, status):
        if (not 'retweeted_status' in status._json) and (not status._json['text'].startswith('RT')):
            global glob_tweet_count
            glob_tweet_count +=1

            with open('tweets.json', 'a') as f:
                f.write(json.dumps(status._json) + '\n')

            print(glob_tweet_count)





    def on_error(self, status_code):
        if status_code == 420:
            return False


