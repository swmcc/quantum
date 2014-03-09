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

## helper functions to get the hashtags mentioned for a given tweet
def hashtags_mentioned(tweet):
    return [ h['text'] for h in tweet['entities']['hashtags'] ]

## helper function to get the users mentioned for a given tweet
def users_mentioned(tweet):
    return [ u['screen_name'] for u in tweet['entities']['user_mentions'] ]
 
def get_most_common(tweets, func, n):
    counter = collections.Counter()

    for tweet in tweets:
        for value in func(tweet):
            counter.update({ value: 1 })

    return counter.most_common(n)

# Output the results to a json file for consumption later
def output_json(data):
    with open('output.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

def go_fish():
    tweets = load_archive()

    output_json({
        'most_mentioned_users': get_most_common(tweets, users_mentioned, 10), 
        'most_mentioned_hashtags': get_most_common(tweets, hashtags_mentioned, 10), 
    })

if __name__ == "__main__":
    go_fish()
