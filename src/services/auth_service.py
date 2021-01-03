from flask_httpauth import HTTPTokenAuth
from requests import HTTPError

from src.dao.firebase import firebase_instance

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(id_token):
    # firebase singleton
    auth = firebase_instance().auth()

    try:
        auth.get_account_info(id_token)
    except HTTPError:
        return False

    return True
