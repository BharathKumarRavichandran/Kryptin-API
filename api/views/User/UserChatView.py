from django.views import generic
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.db.models import Q

from api.models import User, Message
from api.helpers.response_helpers import error_response, invalid_params_response
from api.decorators.response import JsonResponseDecorator


@method_decorator(JsonResponseDecorator, name='dispatch')
class RetrieveChatMessageView(View):

    def post(self, request):

        try:
            from_username   = request.POST.get('fromUsername')
            from_user_token = request.POST.get('token')
            to_username     = request.POST.get('toUsername') 

        except KeyError:
            return invalid_params_response("Invalid parameters")

        try:
            from_user = User.objects.get(username=from_username, token=from_user_token)
            to_user   = User.objects.get(username=to_username)

        except User.DoesNotExist:
            print("Authentication failed/User does not exist")
            return "Authentication failed/User does not exist"

        messages = list(Message.objects.values('from_user', 'to_user', 'message').filter( (Q(from_user=from_user) & Q(to_user=to_user)) | (Q(from_user=to_user) & Q(to_user=from_user)) ).order_by('created_at'))

        return messages