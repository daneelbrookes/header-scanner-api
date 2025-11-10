import requests
from scan_headers import scan_funcs
from typing import Dict, Any

url = 'https://vulnapi.cerberauth.com/docs/best-practices/security-headers'

def scan(url: str) -> Dict[str, Any]:

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
    

    try:
        head = requests.head(url).headers
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

rating = scan(url)
print(rating)