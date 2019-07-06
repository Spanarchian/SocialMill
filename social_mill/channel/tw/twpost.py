import tweepy

consumer_key = 'HRv6CUBKxn7fLMgCE6opjyJNI'
consumer_secret = 'KmqcUkLZvpMdqVejKgUlD9Vb2V7FefuyFYVVf22Aefe7EcSRnw'
access_token = "790162176-c79QQahf3KOM8hg8ioJvlcCq3kqMO0upK347XdNG"
access_token_secret = "UZhAm06J6CoAsr6pRhhH3S7UotDAzO5K0ItupXTAKiLJD"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('Updating using OAuth authentication via Tweepy!')
