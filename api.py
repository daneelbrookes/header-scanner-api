from flask import Blueprint, jsonify, request

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
        return jsonify({"msg": "A URL must be supplied."})
    
    


    return jsonify({"msg": "Yo"})
