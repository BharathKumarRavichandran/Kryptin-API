from django.views import generic
from django.views.generic import View
from django.utils.decorators import method_decorator

from api.models import User
from api.helpers.response_helpers import error_response, invalid_params_response
from api.decorators.response import JsonResponseDecorator

@method_decorator(JsonResponseDecorator, name='dispatch')
class GetOnlineView(View):

    def post(self, request):
        
        try:
            platform = request.POST.get('platform')
            course   = request.POST.get('course')

        except KeyError:
            return invalid_params_response("Invalid parameters")

        status       = True
        online_users = []

        users = User.objects.filter(platform=platform, course=course, status=status)

        for user in users:
            online_users.append({
                'username' : user.username,
                'platform' : user.platform,
                'course'   : user.course
            })

        return online_users


@method_decorator(JsonResponseDecorator, name='dispatch')
class PutOnlineView(View):
    
    def post(self, request):

        try:
            username = request.POST.get('username')
            token    = request.POST.get('token')
            platform = request.POST.get('platform')
            course   = request.POST.get('course')   

        except KeyError:
            return invalid_params_response("Invalid parameters")

        user = User.objects.filter(username=username, token=token, platform=platform, course=course)

        if(user.exists()):
            user.status = True
            user.save()

        else:
            status = True
            user = User.objects.create(username=username, token=token, platform=platform, course=course, status=status)
            return "User status made online"
