import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scan import _scan
import json
import pprint

tests = json.loads(open('testing/test_cases.json').read())

def test_urls():
    for url, ev in tests.items():
        res = _scan(url)

        print("=================================")
        print(url)
        pprint.pprint(res)
        print("=================================")

        
        for header_name, result in res['scan']['headers'].items():

            if header_name not in ev:
                continue

            assert ev[header_name] == result[0], f'URL: {url} FAILED HEADER: {header_name} VAL {result[0]} EV {ev[header_name]}'
