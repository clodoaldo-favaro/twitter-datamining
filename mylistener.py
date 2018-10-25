import tweepy

class Listener(tweepy.StreamListener):


    # Sobrescrever método. on_data = o que vai fazer com os dados? No nosso caso: mostrar o texto e salvar
    def on_data(self, raw_data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(raw_data)
                print(raw_data)
                return True
        except BaseException as e:
            print('Error on_data: {error_message}'.format(error_message = e))
        return True

    def on_error(self, status_code):
        print(status_code)
        return True