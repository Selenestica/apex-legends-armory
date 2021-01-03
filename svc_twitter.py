import twint  # configuration
term = "bitcoin"
config = twint.Config()
config.Search = term
config.Limit = 2  # running search
try:
    config.Hide_output = True
    config.Store_object = True
    twint.run.Search(config)
    res = twint.output.tweets_list
    if len(res) > 0:
        limiter = 0
        body_text = "Tweets:\n"
        for tweet in res:
            print(tweet)
            limiter += 1
            if limiter == 6:
                break
            else:
                body_text += "Username: " + tweet.username
                body_text += "\nDate: " + tweet.datetime
                body_text += "\nTweet: " + tweet.tweet + "\n\n"
    else:
        body_text = "We didn't find any tweets about " + term + "."
except Exception as e:
    print(e)
    body_text = "Error: " + e
print(body_text)
