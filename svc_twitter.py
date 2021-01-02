import twint  # configuration
config = twint.Config()
config.Search = "bitcoin"
config.Limit = 2  # running search
config.Hide_output = True
config.Store_object = True
twint.run.Search(config)

res = twint.output.tweets_list
tweet_list = []
limiter = 0
for tweet in res:
    limiter += 1
    if limiter == 6:
        break
    else:
        tweet_obj = {}
        tweet_obj["username"] = tweet.username
        tweet_obj["tweet"] = tweet.tweet
        tweet_obj["date"] = tweet.datetime
        tweet_list.append(tweet_obj)
print(tweet_list)
