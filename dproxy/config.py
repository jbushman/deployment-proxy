import os
import logging

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv(".env")


class Config(object):
    HOSTNAME = os.getenv("HOSTNAME")
    IP = os.getenv("IP")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    STATE = os.getenv("STATE")
    LOCATION = os.getenv("LOCATION")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    TOKEN = os.getenv("TOKEN")
    DEPLOYMENT_PROXY_URI = os.getenv("DEPLOYMENT_PROXY_URI")
    DEPLOYMENT_API_URI = os.getenv("DEPLOYMENT_API_URI")

    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    CELERY_TASK_SERIALIZER = os.getenv("CELERY_TASK_SERIALIZER")
    CELERY_RESULT_SERIALIZER = os.getenv("CELERY_RESULT_SERIALIZER")
    CELERY_ACCEPT_CONTENT = os.getenv("CELERY_ACCEPT_CONTENT")
    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE")
    CELERY_UTC = os.getenv("CELERY_UTC")


def get_logger():
    logger = logging.getLogger("bhdapi")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("/opt/deployment/proxy/dproxy.log")
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

