#!/usr/bin/env python

import json, glob 
from pprint import pprint

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

def go_fish():
    tweets = load_archive()
    pprint(tweets)

if __name__ == "__main__":
    go_fish()
