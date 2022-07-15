import tweepy
import pymongo
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'Toulouse -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10)

tweets = response.data


#for tweet in response.data:
#    tweets.append(tweet)


myclient = pymongo.MongoClient(config.URL + ":" + config.PORT + "/")

mydb = myclient["dataming"]

mycol = mydb["TFC"]

mycol.insert_many(tweets)