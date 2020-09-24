import os
import requests
from flask import request

from dproxy.config import Config
from dproxy.tasks.deployment.tasks import rollout
from dproxy.config import get_logger
logger = get_logger()


def post_rollout():
    data = request.get_json()
    try:
        rollout.apply_async(args=[data])
        response = {
            "status": "success",
            "message": "Rollout successfully started",
        }
        return response, 202
    except Exception as e:
        response = {
            "status": "failure",
            "message": "Rollout failed to start",
            "exception": str(e)
        }
        return response, 409
