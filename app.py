#!/usr/bin/env python

import json, glob 
from pprint import pprint

for file in glob.glob('data/js/tweets/*.js'):
    with open(file) as data:
        # skip that annoying first line
        raw_data = data.readlines()[1:]
        raw_data = "".join(raw_data)
        raw_json = json.loads(raw_data)
        data.close()
        pprint(raw_json)

