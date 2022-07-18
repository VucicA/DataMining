import tweepy
import pymongo
import config
import json
from pprint import pprint

mongoDB = pymongo.MongoClient("mongodb+srv://VucicA:7cCFuJ1udrMNe0OY@tfc.jcz2iy9.mongodb.net/?retryWrites=true&w=majority")
mydb = mongoDB.datamining
mycol = mydb.TFC

twitter = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = '"Toulouse FC" lang:fr -is:retweet '

response = twitter.search_recent_tweets(query=query, 
                                        max_results=100, #max 100
                                        tweet_fields=[
                                            'text',
                                            'public_metrics',
                                            'created_at',
                                            'geo'
                                        ])

tweets = response.data

for tweet in tweets:
    sendJson = {
        'id' : tweet.id,
        'text' : tweet.text,
        'geo' :tweet.geo,
        'created_at' : tweet.created_at,
        'public_metrics' : tweet.public_metrics
    }

    pprint(sendJson)

    mycol.insert_one(sendJson)