from flask import Flask, render_template
app = Flask(__name__)

# class to help render the tweets  
class Tweet: 
    def _init_(self, message, time, done, row_idx):
        self.message = message
        self.time = time
        self.done = done
        self.row_idx = row_idx


@app.route('/')
def hello_world():
    return('hello world')
    # tweets = []
    # for idx, tweet in enumerate(tweet_records)
    # n_open_tweets=sum(1 for tweet in tweets if not tweet.done)
    # return render_template('base.html', tweets=tweets, n_open_tweets=n_open_tweets )