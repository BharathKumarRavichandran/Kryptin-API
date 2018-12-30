from django.contrib.sessions.models import Session

from django.core.validators import validate_email as _validate_email
from django.core.exceptions import ValidationError

from random import choice
from string import ascii_letters, digits
import time
import os

from api.models import User


def remove_existing_sessions(user_id):
    """
    Removes sessions on other devices for the giver user_id
    """
    sessions = Session.objects.all()

    for session in sessions:
        data = session.get_decoded()
        if data.get('user_id', -1) == user_id:
            # Already a session exist, delete it
            session.delete()
    return


def validate_email(email):
    try:
        _validate_email(email)
        return True
    except ValidationError:
        return False
        

def generate_auth_token(length=30):
    '''
    Generates a random string of the given length containing ascii letters and
    digits.
    Args:
        length(int)[optional] : Describing the length of the required auth token
    Returns:
        auth_token : A random string of given length
    '''

    auth_token_domain = ascii_letters + digits
    auth_token        = ''.join(choice(auth_token_domain) for i in range(length))
    auth_token        = auth_token+str(time.time())

    return auth_token
