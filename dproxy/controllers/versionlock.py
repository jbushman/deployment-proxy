import requests
from flask import request
from dproxy.util.http_helper import get_http


def post_versionlock():
    data = request.get_json()
    try:
        if "hostname" in data:
            r = requests.post(f"http://{data['hostname']}:8003/versionlock", json=data)
            resp = r.json()
            return resp, 201
        else:
            response = {
                "status": "failed",
                "message": "Unable to find Base64 encoded client url.",
            }
            return response, 409
    except Exception as e:
        raise Exception(f"Unable to Post versionlock: {e}")


def get_versionlock(hostname):
    try:
        http = get_http
        r = http.get(f"http://{hostname}:8003/versionlock", json=data)
        resp = r.json()
        return resp, 201
    except Exception as e:
        raise Exception(f"Unable to Get versionlock: {e}")
