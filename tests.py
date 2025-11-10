from scan import _scan

#https://developer.mozilla.org/en-US/observatory/analyze?host=www.youtube.com
def test_youtube():

    ev = {
        "strict-transport-security": 0,
        "x-content-type-options": 0,
        "set-cookie": 0,
        "referrer-policy": 0
    }

    res = _scan('https://youtube.com')

    for header_name, result in res['scan']['headers'].items():
        assert(ev[header_name] == result[0])

def test_mozilla():

    ev = {
        "strict-transport-security": 0,
        "x-content-type-options": 0,
        "set-cookie": 0,
        "referrer-policy": 5
    }

    res = _scan('https://developer.mozilla.org/en-US/observatory')

    for header_name, result in res['scan']['headers'].items():
        assert(ev[header_name] == result[0])