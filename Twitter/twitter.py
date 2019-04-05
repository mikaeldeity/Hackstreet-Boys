# importing the module 
import tweepy 
  
# personal details 
consumer_key ="YRPJJWFyaTmtsaYBphX8xu1gv"
consumer_secret ="yeZdc13Mb64kZjvRxtQDqdYVW6zstLWumiupNwrZkdAC6SoN0u"
access_token ="4848975431-V7mYuLGeIyLueg3x4Oe2pl1UP3ERerqqXBvhq8x"
access_token_secret ="c7oDMSUSksWpsJMYje13cC9KwovwzPhmSLf3l4yBKUtTt"
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status ="Hackstreet Boys!") 

#tweet with python
"""

# importing the module 
import tweepy 
  
# personal information 
consumer_key ="xxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxx"
  
# authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
   
api = tweepy.API(auth) 
tweet ="Text part of the tweet" # toDo 
image_path ="path of the image" # toDo 
  
# to attach the media file 
status = api.update_with_media(image_path, tweet)  
api.update_status(status = tweet) 

"""