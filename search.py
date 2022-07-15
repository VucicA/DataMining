import tweepy
import pymongo
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'from:Toulouse FC -is:retweet'

response = client.search_recent_tweets(query=query, max_results=100)

tweets = []


for tweet in response.data:
    tweets.append(tweet)


myclient = pymongo.MongoClient(config.URL + ":" + config.PORT + "/")


dblist = myclient.list_database_names()
if "dataming" in dblist:
    print("The database exists.")
else :
    mydb = myclient["dataming"]


collist = mydb.list_collection_names()
if "TFC" in collist:
  print("The collection exists.")
else:
    mycol = mydb["TFC"]

mycol.insert_one(tweets)