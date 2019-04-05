# importing the module 
import tweepy 
  
# personal details 
consumer_key ="fhazovCsZr1omSLxEaLCnnwpY"
consumer_secret ="RUlFSGumpW54s5m1r5er4m5laqhsXRkr21lgsGFFQ9emyl9Mt8"
access_token ="1114137250466549761-4TiU60hxfrIRuYQrUaTq0XKVMfSnLR"
access_token_secret ="EapPYjEGFeRAaKIhvchB59WBUWRGOK5FlpBqZkFF9PTTj"
  
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