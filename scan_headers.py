# 
# https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring


from typing import Tuple

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
        return (-5, "X-Content-Type-Options header not implemented")

    if val.lower() == 'nosniff':
        return (0, "X-Content-Type-Options header set to nosniff")
    
    return (-5, "X-Content-Type-Options header cannot be recognized")

@scan_header("set-cookie")
def set_cookie(val: str) -> Tuple[int, str]:

    if val is None:
        return (0, "No cookies detected")

    cookies = val.split(";")

    #if 'Secure' in cookies:

    return (0, "")

@scan_header("referrer-policy")
def referrer_policy(val: str) -> Tuple[int, str]:

    if val is None:
        return (0, "Referrer-Policy header not implemented")

    if val in [
        "no-referrer",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin"
    ]:
        return (5, "Referrer-Policy header set to no-referrer, same-origin, strict-origin or strict-origin-when-cross-origin")
    
    elif val in [
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
        "no-referrer-when-downgrade"
    ]:
        return (-5, "Referrer-Policy header set unsafely to origin, origin-when-cross-origin, unsafe-url or no-referrer-when-downgrade")
    
    return (-5, "Referrer-Policy header cannot be recognized")

@scan_header('accept-control-allow-origin')
def accept_control_allow_origin(val: str) -> Tuple[int, str]:
    
    return (0, "")

@scan_header('x-frame-options')
def x_frame_options(val: str) -> Tuple[int, str]:

    if val is None:
        return (-20, "X-Frame-Options (XFO) header not implemented")
    
    if val in ['SAMEORIGIN', 'DENY']:
        return (0, "X-Frame-Options (XFO) header set to SAMEORIGIN or DENY")
    

    return (-20, "X-Frame-Options (XFO) header cannot be recognized")





# to-do, this is complicated x)

# @scan_header("content-security-policy")
# def content_security_policy(val: str) -> Tuple[int, str]:

#     if val is None:
#         return (-25, "Content Security Policy (CSP) header not implemented")

