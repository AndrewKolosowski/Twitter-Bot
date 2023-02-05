import tweepy
import time
from selenium import webdriver
import os
#API Information
api_key = 'fSx85o845K8oHv54hY1fZMrdB'
api_secret = 'FCZlyXt06hDwAqVOAialKn2PsTYgtQQ5ecgvSpWpACaNNqbwaq'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAoslgEAAAAA2Ywbt0%2FAulugTdv6lqRPV5LwoxY%3Dr4trVtbiDJeH5ouxczvc3sguPZf0CRVBtFhx57J3IKo44lWQMG'
access_token = '3667934417-q5Aq82H1cogono7t8Czx1jEOXaL9OhMMSgbjN2T'
access_token_secret = 'pPyOUTDKr5QC84sghWSROrIrSl4n04vfJx0ilBAsCongn'

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


class MyStream(tweepy.StreamingClient):

#Gets called when a tweet is made that meets the criteria of the stream filter
    def on_tweet(self, tweet):
        tweetID = str(tweet.id)
        username = str(client.get_user(id=tweet.author_id).data)
        print(username + " made a tweet that says: " + tweet.text)
        screenshotter(tweetID, username)

#Takes screenshot
def screenshotter(tweetID, username):
    browser = webdriver.Firefox()
    url = 'https://twitter.com/' + username + '/status/' + tweetID
    if not os.path.isdir('D:/python/TwitterBot/Screenshot Folder/' + username):
        os.makedirs('D:/python/TwitterBot/Screenshot Folder/' + username)
    path = 'D:/python/TwitterBot/Screenshot Folder/' + username + '/' + tweetID + '.png'
    browser.get(url)
    time.sleep(5)
    browser.save_screenshot(path)
    browser.quit()


# Creating Stream object
stream = MyStream(bearer_token=bearer_token)
print(stream.get_rules())
rule_ids = []
result = stream.get_rules()

for rule in result.data:
    print(f"rule marked to delete: {rule.id} - {rule.value}")
    rule_ids.append(rule.id)

if(len(rule_ids) > 0):
    stream.delete_rules(rule_ids)
else:
    print("no rules to delete")
stream.add_rules(tweepy.StreamRule("from:Cobratate OR from:ChrisBoshesMom OR from:FoxNews OR from:CNN OR from:cp24 OR from:test OR from:test1 OR from:test2 OR from:test3 OR from:test4 OR from:test5 OR from:test6 OR from:test7 OR from:test8 OR from:test9 OR from:test10 OR from:test11 OR from:test12 OR from:test13 OR from:test14 OR from:test15 OR from:test16 OR from:test17 OR from:test18 OR from:test19 "))
print(stream.get_rules())
stream.filter(tweet_fields=['author_id'])