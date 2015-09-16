import time
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#Import sys for command line changes
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

open('twitter_data.txt', 'w').close()
#Variables that contains the user credentials to access Twitter API
access_token = "2826782509-gHsY9mwiaIoH1x8cGxVxAe1348fVN23weWQLTcd"
access_token_secret = "W2ctcnve2GmW4xOmKfcwBdMXJqddH4A9sykwiv6MnhgWG"
consumer_key = "8vq19xpavMHQA8kQ51yR1PRgx"
consumer_secret = "dQcf06syfPXtyMY6uIZiqNbJG1HUkwTklcSCuhhSm7cW6cGBRL"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        time.clock()
        data_file = open('twitter_data.txt', 'a')
        data_file.write(data)
        data_file.close()
        if time.clock()>15:
            return False
        return True
    def on_error(self, status):
        print status
 
def grab_tweets():
    #This handles Twitter authentification and the connection to Twitter Streaming API
    time.clock()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the argument variable keyword.
    print "before filter"
    a=str(sys.argv[1])
    stream.filter(track=[a])
    print "after filter"
    return
#this is now appending each new data point to a list
if __name__ == "__main__":
    alltweetsdata=[]
    alltimedata=[]
while __name__ == '__main__':
    grab_tweets()
    first=time.clock()
    print "did it "
    f=open("twitter_data.txt", "r")
    tweets_data=0
    for line in f:
        if sys.argv[1] in line:
            tweets_data+=1
    alltweetsdata.append(tweets_data)
    alltimedata.append(first)
    print 'Number of matching tweets: %s' % alltweetsdata
    print "Time information: %s" % alltimedata
#This is plotting the information starting with 2 points
    if len(alltimedata)>1:
    	plt.plot(alltimedata, alltweetsdata)
    	plt.show()
    print "good"
 
