import tweepy
from queue import Queue
from threading import Thread

glob_tweet_count = 0


class Listener(tweepy.StreamListener):


    def __init__(self, q = Queue()):
        print('init da classe')
        super().__init__()
        num_worker_threads = 4
        self.q = q
        for i in range(num_worker_threads):
            t = Thread(target=self.salvar_tweet())
            t.daemon = True
            t.start()


    def salvar_tweet(self):
        while True:
            tweet = self.q.get()
            if (not tweet._json['retweeted']) and (not tweet._json['text'].startswith('RT @')):
                try:
                    with open('tweets.json', 'a') as f:
                        f.write(tweet + '\n')
                        global glob_tweet_count
                        glob_tweet_count += 1
                        print(glob_tweet_count)
                except BaseException as e:
                    print('Error on_data: {error_message}'.format(error_message=e))

        return True



    def on_status(self, status):

        if not status.retweeted_status:
            print(status.text)
            self.q.put(status)




    def on_error(self, status_code):
        if status_code == 420:
            return False


