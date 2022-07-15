import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'from:Toulouse FC -is:retweet'

response = client.search_recent_tweets(query=query, max_results=100)

for tweet in response.data:
    print(tweet.id)
    