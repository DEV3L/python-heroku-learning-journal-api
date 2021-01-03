import json
import os

import pyrebase

FIREBASE_API_KEY = os.environ.get("FIREBASE_API_KEY", "api_key")
FIREBASE_AUTH_DOMAIN = os.environ.get("FIREBASE_AUTH_DOMAIN", "auth_domain")
FIREBASE_DATABASE_URL = os.environ.get("FIREBASE_DATABASE_URL", "database_url")
FIREBASE_STORAGE_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET", "storage_bucket")
FIREBASE_ADMIN_PRIVATE_KEY = os.environ.get("FIREBASE_ADMIN_PRIVATE_KEY", "admin_private_key")

SERVICE_ACCOUNT_PATH = "./data/firebase-adminsdk.json"
SERVICE_ACCOUNT_PATH_TEMP = "./data/_firebase-adminsdk.json"

config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
    "serviceAccount": SERVICE_ACCOUNT_PATH_TEMP
}

_firebase = None


def firebase_instance():
    global _firebase

    if _firebase:
        return _firebase

    # handle newlines
    firebase_admin_private_key = FIREBASE_ADMIN_PRIVATE_KEY.replace("\\n", "\n")

    with open(SERVICE_ACCOUNT_PATH) as service_account_file:
        service_account_json = json.load(service_account_file)

    service_account_json['private_key'] = firebase_admin_private_key

    with open(SERVICE_ACCOUNT_PATH_TEMP, 'w') as temp_service_account_file:
        json.dump(service_account_json, temp_service_account_file)

    _firebase = pyrebase.initialize_app(config)
    return _firebase
