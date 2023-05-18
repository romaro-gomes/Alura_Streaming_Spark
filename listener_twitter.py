import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s=socket.socket()

s.bind((HOST,PORT))

print(f"Aguardando conxexão com a  porta: {PORT}")

s.listen()

connection, endereco=s.accept()

print(f"Recebendo solicitação de {endereco}")

token="AAAAAAAAAAAAAAAAAAAAAJQCiAEAAAAAumemSFotG90ndqxUGEKavyJOVjk%3DX5mELPKtrM1wqPIt56yIcXgc6wkLxIZlj81ZifoMklWLKV03IC"
keyword="DNA"

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self,tweet):
        print(tweet.text)
        print("=*="*25)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()


connection.close()

        
