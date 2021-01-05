import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
# import pandas
search_by = "keyword"
search_arg = "bitcoin"
todays_date_str = datetime.today().strftime('%Y-%m-%d')
yesterdays_date = datetime.now() - timedelta(1)
yesterdays_date_str = datetime.strftime(yesterdays_date, '%Y-%m-%d')
if search_by == "keyword":
    scrape_crit = f"{search_arg} since:{yesterdays_date_str} until:{todays_date_str}"
    body_text = f"Tweets about {search_arg}:\n\n"

elif search_by == "username":
    scrape_crit = f"from:{search_arg}"
    body_text = f"Tweets by {search_arg}:\n\n"

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(scrape_crit).get_items()):
    # print(vars(tweet))
    # print(vars(tweet.user))
    if i > 9:
        break
    date_str = tweet.date.strftime("%Y-%d-%m")
    body_text += f"Name: {tweet.user.displayname} ({tweet.user.username})\n"
    body_text += f"Date: {date_str}\n"
    body_text += f"Tweet: {tweet.content}\n\n"

print(body_text)

"""

Attributes available through snscrape tweet object

url: link pointing to tweet location
date
content
renderedcontent: same as above
id
user: {username, display name, user id, user bio, url in bio, verified boolean, date account created, follower count, friend count, total tweets,
    favourite count, listed count, media count, account location, private boolean, profile image url, profile banner url}
outlinks
tcooutlinks
replyCount
retweetCount
likeCount
quoteCount
conversationId: same as tweet id
lang: language of tweet
source: where tweet was posted from
media: if tweet contains media, has links pointing to preview version and full version
retweetedTweet: if retweet, id of og tweet
quotedTweet: if quoted tweet, id of og
mentionedUsers: user objects of any mentioned user in tweet

{'url': 'https://twitter.com/breakfasttaco3/status/1345543401878528000', 'date': datetime.datetime(2021, 1, 3, 1, 32, tzinfo=datetime.timezone.utc), 'content': 'This is my first tweet. Hello world :)', 'renderedContent': 'This is my first tweet. Hello world :)', 'id': 1345543401878528000, 'user': User(username='breakfasttaco3', displayname='breakfast_taco', id=1341552760395841536, description='', rawDescription='', descriptionUrls=[], verified=False, created=datetime.datetime(2020, 12, 23, 1, 16, 11, tzinfo=datetime.timezone.utc), followersCount=0, friendsCount=7, statusesCount=1, favouritesCount=0, listedCount=0, mediaCount=0, location='', protected=False, linkUrl=None, linkTcourl=None, profileImageUrl='https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', profileBannerUrl=None), 'outlinks': [], 'tcooutlinks': [], 'replyCount': 0, 'retweetCount': 0, 'likeCount': 0, 'quoteCount': 0, 'conversationId': 1345543401878528000, 'lang': 'en', 'source': '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>', 'sourceUrl': 'https://mobile.twitter.com', 'sourceLabel': 'Twitter Web App', 'media': None, 'retweetedTweet': None, 'quotedTweet': None, 'mentionedUsers': None}
{'username': 'breakfasttaco3', 'displayname': 'breakfast_taco', 'id': 1341552760395841536, 'description': '', 'rawDescription': '', 'descriptionUrls': [], 'verified': False, 'created': datetime.datetime(2020, 12, 23, 1, 16, 11, tzinfo=datetime.timezone.utc), 'followersCount': 0, 'friendsCount': 7, 'statusesCount': 1, 'favouritesCount': 0, 'listedCount': 0, 'mediaCount': 0, 'location': '', 'protected': False, 'linkUrl': None, 'linkTcourl': None, 'profileImageUrl': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profileBannerUrl': None}

"""
