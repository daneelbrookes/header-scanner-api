import requests
from scan_headers import scan_funcs

url = 'https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring'

def scan(url: str):

    rating = 0

    head = requests.head(url).headers
    print(head)

    for header, func in scan_funcs.items():
        
        header_val = head.get(header.lower(), None)
        rating += func(header_val)

    return rating

rating = scan(url)
print(rating)