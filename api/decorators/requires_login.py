from django.http import HttpRequest

from api.models import User
from django.contrib.sessions.models import Session
from api.helpers.response_helpers import unauthorized_response


def RequiresLoginDecorator(view):
    """
    Checks whether the current session is up-to-date with the
    sessions in the backend
    """

    def wrapper(*args, **kwargs):

        try:
            request = args[0]
            assert isinstance(request, HttpRequest)

            user_id      = request.session.get('user_id')
            session_key  = request.session.session_key
            user_session = Session.objects.get(pk=session_key)

            assert user_session.get_decoded().get('user_id') == user_id

            user = User.objects.get(pk=user_id)
            whitelisted_path = []

        except Exception as e:
            return unauthorized_response()

        return view(*args, **kwargs)

    return wrapper
