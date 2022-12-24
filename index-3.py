from flask import *
# from logging import FileHandler,WARNING
import json, time

app = Flask(__name__)
# app = Flask(__name__, template_folder = 'template')
# file_handler = FileHandler('errorlog.txt')
# file_handler.setLevel(WARNING)
# ----------------------------------

from flask_cors import CORS

CORS(app)
cors= CORS (app, resources={
    r"/*" : {
        "origins" : "*"
    }
})

import snscrape.modules.twitter as sntwitter
# import pandas as pd

# query = "python"
query = "(from:fabrizioromano)"
# tweets = []
# limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # tweet = json.dumps(tweet)
    print(vars(tweet))
    break 
    # if len(tweets) == limit:
    #     break
    # else:
    #     tweets.append([tweet.date, tweet.username, tweet.content])
        
# df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# print(df)

# ----------------------------------


@app.route('/', methods=['GET'])
def home_page():
    # data_set = {'name':'ronaldo', 'message':'Hello from portugal'}
    # json_dump = json.dumps(data_set)

    # print(
    return vars(tweet)

if __name__ == '__main__':
    app.run(port=7777)