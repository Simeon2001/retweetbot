import tweepy
import logging
import time
import random
from datetime import datetime, timedelta
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()

def retweet_tweets_with_hashtag(api, need_hashtags):
    if type(need_hashtags) is list:
        search_query = f"{need_hashtags} -filter:retweets"
        tweets = api.search(q=search_query, lang ="en", tweet_mode='extended')
        for tweet in tweets:
            hashtags = [i['text'].lower() for i in tweet.__dict__['entities']['hashtags']]
            try:
                need_hashtags = [hashtag.strip('#') for hashtag in need_hashtags]
                need_hashtags = list(need_hashtags)
                if set(hashtags) & set(need_hashtags):
                    if tweet.user.id != api.me().id:
                        api.retweet(tweet.id)
                        logger.info(f"Retweeted tweet from {tweet.user.name}")
                        time.sleep(5)
            except tweepy.TweepError:
                logger.error("Error on retweet", exc_info=True)
    else:
        logger.error("Hashtag search terms needs to be of type list", exc_info=True) 
        return
a = ["#ENDSARSNOW","#SARSMUSTEND","#SARSMUSTENDNOW","#EndPoliceBrutalityinNigeria","#togetherwecan"]
    c=b
while True:
    for b in a:
        retweet_tweets_with_hashtag(api, [b])
    logger.info("Waiting...")
    time.sleep(30)
    
    