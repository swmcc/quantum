#!/usr/bin/env python

import collections, json, glob 
from collections import Counter
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

def get_most_mentioned(tweets):
    users = []
    for tweet in tweets:
        for user in tweet['entities']['user_mentions']:
            users.append(user['screen_name'])
    return collections.Counter(users).most_common(10)


def go_fish():
    tweets = load_archive()
    most_mentoined_users = get_most_mentioned(tweets)


if __name__ == "__main__":
    go_fish()
