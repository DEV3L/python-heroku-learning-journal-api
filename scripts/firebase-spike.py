from dotenv import load_dotenv

load_dotenv()

from src.dao.firebase import firebase_instance

id_token = "id_token"

if __name__ == '__main__':
    firebase = firebase_instance()
    auth = firebase.auth()
    account_info = auth.get_account_info(id_token)

    print(account_info)
