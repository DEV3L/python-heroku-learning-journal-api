from flask import Blueprint

from src.services.auth_service import auth

ping = Blueprint('ping', __name__)


@ping.route('/', methods=['GET'])
@ping.route('/ping', methods=['GET'])
def hello_world():
    """
    Monitor endpoint
    ---
    tags:
      - ping
    responses:
      200:
        description: Hello, world!
    """
    return 'Hello, world!'


@ping.route('/ping_authenticated', methods=['GET'])
@auth.login_required
def hello_world_authenticated():
    """
    Authenticated monitor endpoint
    ---
    tags:
      - ping_authenticated
    responses:
      200:
        description: Hello, authenticated world!
    """
    return 'Hello, authenticated world!'


@ping.route('/raise', methods=['GET'])
def raise_exception():
    raise RuntimeError('500 status code')
