import tweepy
import pymongo
import config
import json

mongoDB = pymongo.MongoClient(config.URL + ":" + config.PORT + "/")
mydb = mongoDB.datamining
mycol = mydb.TFC

twitter = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = '"Toulouse FC" lang:fr -is:retweet'

response = twitter.search_recent_tweets(query=query, max_results=10)

tweets = response.data


for tweet in tweets:
    sendJson = {
        'id' : tweet.id,
        'text' : tweet.text
    }
    print(sendJson)
    mycol.insert_one(sendJson)