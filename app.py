#!/usr/bin/env python

import collections, json, glob 
from collections import Counter
from pprint import pprint

# Load the archive into memory
def load_archive():
    tweets = []
    for file in glob.glob('data/js/tweets/*.js'):
        with open(file) as data:
            # skip that annoying first line
            raw_data = data.readlines()[1:]
            raw_data = "".join(raw_data)
            raw_json = json.loads(raw_data)
            data.close()
            for tweet in raw_json:
                tweets.append(tweet)
    return sorted(tweets, key=lambda k: k['id'])

# Most mentioned users I tweet about 
def get_most_mentioned(tweets):
    users = {} 
    for tweet in tweets:
        for user in tweet['entities']['user_mentions']:
            users.append(user['screen_name'])
    return collections.Counter(users).most_common(10)

# Most hashtags I use
def get_most_hashtags(tweets):
    hashtags = []
    for tweet in tweets:
        for hashtag in tweet['entities']['hashtags']:
            hashtags.append(hashtag['text'])
    return collections.Counter(hashtags).most_common(10)

# Output the results to a json file for consumption later
def output_json(data):
    with open('output.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

def go_fish():
    tweets = load_archive()
    json = {
      'most_mentioned_users': get_most_mentioned(tweets), 
      'most_mentioned_hashtags': get_most_hashtags(tweets) 
    }

    output_json(json)

if __name__ == "__main__":
    go_fish()
