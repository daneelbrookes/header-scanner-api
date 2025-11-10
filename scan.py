import requests
from scan_headers import scan_funcs
from typing import Dict, Any

url = 'https://vulnapi.cerberauth.com/docs/best-practices/security-headers'

def _scan(url: str) -> Dict[str, Any]:

    """
    
    {
        "status": SUCCESSFUL, FAILED,
        "err_msg": str,
        "scan":
        {
            rating: int,
            headers: Dict[str, Tuple[int, str]] -> for example {"strict-transport-security": (-20, "Header not implemented")}
        }
    }
    
    """

    rating = 0
    header_tuples = {}
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'http://www.google.com/',
        'Connection': 'keep-alive'
    }
    
    try:
        head = requests.head(url, headers=send_headers, allow_redirects=True).headers
    except requests.ConnectionError:
        return {
            "status": "FAILED",
            "err_msg": "URL could not be resolved",
            "scan": {}
        }


    for header, func in scan_funcs.items():
        
        header_val = head.get(header.lower(), None)

        score, msg = func(header_val)

        rating += score
        header_tuples[header.lower()] = (score, msg)


    return {
        "status": "SUCCESSFUL",
        "err_msg": None,
        "scan": {
            "rating": rating,
            "headers": header_tuples
        }
    }
