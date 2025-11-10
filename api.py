from flask import Blueprint, jsonify, request
from scan import _scan

api = Blueprint("api", __name__)

@api.route("/scan", methods=["POST"])
def scan():

    """
    
    Args:
    url (str): URL to scan

    """

    data = request.get_json()

    url = data.get('url') if data else None
    if url is None:
        return jsonify(
            {
                "status": "SUCCESSFUL",
                "err_msg": "",
                "scan": {}
            }
        )
    
    resp = _scan(url)
    
    return jsonify(resp)
