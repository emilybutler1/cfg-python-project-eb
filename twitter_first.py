import tweepy

consumer_key = 'bR2J5tAC3i8r6X1ZY7V1DgrFs'
consumer_secret = 'N4Pxa8WRC54sW2cbOyV7zk7pXvfgAKZn1fDlhTg2cc1QKzVJ0O'
access_token = '4758617309-6aZMcsGEkFmeJCbhjsN8fWMleFy3ROlurowzf6h'
access_token_secret = '9Aby0uHgrpSisjej1Kndn35Zba4ODCvT8nlscaANek97J'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

print('Logged in as {}'.format(twitter_api.me().name))

