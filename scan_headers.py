from typing import Tuple

"""

Good Headers:

https://vulnapi.cerberauth.com/docs/best-practices/security-headers
https://developer.mozilla.org/en-US/observatory/analyze?host=youtube.com#scoring

Strict-Transport-Security
Cross-Origin-Opener-Policy
Content-Security-Policy
X-Frame-Options
X-Content-Type-Options
X-XSS-Protection
Set-Cookie (Secure, HttpOnly)

"""

scan_funcs = {}

def scan_header(header_name: str):
    def decorator(func):
        scan_funcs[header_name] = func
        return func
    return decorator

@scan_header("strict-transport-security")
def strict_transport_security(val: str) -> Tuple[int, str]:

    # No header exists
    if val is None:
        return (-20, "Header not implemented")
    
    list_val = val.split(";")
    age = None
    
    for val in list_val:
        if 'max-age' in val:
            try:
                age = int(val.split('=')[1])
            except ValueError:
                # Invalid header
                return (-20, "Header not recognized")
                    
    if age is None:
        return (-20, "Header not recognized")
    
    if age < 15768000:
        return (-10, "Header set to less than six months")
    
    if 'preload' in list_val:
        return (5, "Header is preloaded")
    
    return (0, "Header set to a minimum of six months")

@scan_header("x-content-type-options")
def x_content_type_options(val: str) -> Tuple[int, str]:

    if val is None:
        return (-5, "")

    if val.lower() == 'nosniff':
        return (0, "")
    
    return (-5, "")

@scan_header("set-cookie")
def set_cookie(val: str) -> Tuple[int, str]:

    if val is None:
        return (0, "")

    cookies = val.split(";")

    #if 'Secure' in cookies:

    return (0, "")

@scan_header("referrer-policy")
def referrer_policy(val: str) -> Tuple[int, str]:

    if val is None:
        return (0, "")

    if val in [
        "no-referrer",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin"
    ]:
        return (5, "")
    
    elif val in [
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
        "no-referrer-when-downgrade"
    ]:
        return (-5, "")
    
    return (-5, "")
    
