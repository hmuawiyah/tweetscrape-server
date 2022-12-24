from flask import *
from flask_cors import CORS
# import json, time
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

CORS(app)
cors= CORS (app, resources={
    r"/*" : {
        "origins" : "*"
    }
})

# @app.route('/<tweetnya>', methods=['GET'])
# def home_page(tweetnya):

@app.route('/s', methods=['GET'])
def home_page():
    args = request.args
    tweetnya = args.get('tweetnya')

    # query = "(from:fabrizioromano)"

    for tweet in sntwitter.TwitterSearchScraper(tweetnya).get_items():
        print(vars(tweet))
        break 

    return vars(tweet)
    # return tweetnya

if __name__ == '__main__':
    app.run(port=7777)