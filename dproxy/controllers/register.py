from dproxy.util.config import Config

import os
import requests
from flask import request
from flask import current_app as app


def post_register_server():
    data = request.get_json()
    try:
        app.logger.debug(f"POST REGISTER SERVER: {data}")
        r = requests.post(f"{Config.DEPLOYMENT_API_URI}/register/server", json=data)
        resp = r.json()
        app.logger.debug(f"RESPONSE REGISTER SERVER: {resp}")
        response = {
            "status": "success",
            "message": "Server successfully registered",
            "server": resp["server"],
            "token": resp["token"],
        }
        return response, 201
    except Exception as e:
        response = {
            "status": "failure",
            "message": "Register server failed",
            "exception": str(e),
        }
        return response, 409
