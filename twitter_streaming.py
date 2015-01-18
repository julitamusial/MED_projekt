#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2951115861-peahndTg3uECWB8sLwYoQx4bFsOhcYrfybgx9EH"
access_token_secret = "hwoUiCMIfpa1H41ZXwTGub2jKubKh71EVgwMCBlLY8Vcd"
consumer_key = "uaAmflZeF8x91WeLraPcu76y0"
consumer_secret = "cg6esQZ1hBf5QmV9yNf0qMRQdzVn8BQ93ZcvL9SirHfKVpdFoW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(locations = [-118.30876350402832, 33.99916579100914, -118.1356430053711, 34.07029354225064])
