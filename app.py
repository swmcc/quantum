#!/usr/bin/env python

import json
from pprint import pprint

with open('test.json') as json_data:
    d = json.load(json_data)
    json_data.close()
    pprint(d)

