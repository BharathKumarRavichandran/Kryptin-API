from django.views import generic
from django.views.generic import View
from django.utils.decorators import method_decorator

from api.models import User, Course
from api.helpers.response_helpers import error_response, invalid_params_response
from api.decorators.requires_login import RequiresLoginDecorator
from api.decorators.response import JsonResponseDecorator

@method_decorator(JsonResponseDecorator, name='dispatch')
@method_decorator(RequiresLoginDecorator, name='dispatch')
class GetOnlineView(View):

    def post(self, request):
        
        try:
            user_id    = request.SESSION.get('user_id')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')

        except KeyError:
            return invalid_params_response("Invalid parameters")

        status       = True
        online_users = []

        users = Course.objects.values('user_id__username', 'platform','coursename').filter(platform=platform, coursename=coursename, status=status).exclude(email=email)

        for user in users:
            online_users.append({
                'username'   : user['username__username'],
                'platform'   : user['platform'],
                'coursename' : user['coursename']
            })

        return online_users


@method_decorator(JsonResponseDecorator, name='dispatch')
@method_decorator(RequiresLoginDecorator, name='dispatch')
class PutOnlineView(View):
    
    def post(self, request):

        try:
            user_id    = request.SESSION.get('user_id')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')  
            status     = True

        except KeyError:
            return invalid_params_response("Invalid parameters")

        course = ""
        user   = ""

        user = User.objects.get(pk=user_id)

        try:
            course = Course.objects.get(user_id=user, platform=platform, coursename=coursename)

        except Course.DoesNotExist:
            course = Course.objects.create(user_id=user, platform=platform, coursename=coursename, status=status)
            print("User course created and status made online")
            return "User course created and status made online"           

        if course is not None:
            course.status = status
            course.save()
            print("User status made online")
            return "User status made online"
            

@method_decorator(JsonResponseDecorator, name='dispatch')
@method_decorator(RequiresLoginDecorator, name='dispatch')
class PutOfflineView(View):
    
    def post(self, request):

        try:
            user_id    = request.SESSION.get('user_id')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')  
            status     = False

        except KeyError:
            return invalid_params_response("Invalid parameters")

        course = ""
        user   = ""

        user = User.objects.get(pk=user_id)

        try:
            course = Course.objects.get(user_id=user, platform=platform, coursename=coursename)

        except Course.DoesNotExist:
            course = Course.objects.create(user_id=user, platform=platform, coursename=coursename, status=status)
            print("User course created and status made offline")
            return "User course created and status made offline"           

        if course is not None:
            course.status = status
            course.save()
            print("User status made offline")
            return "User status made offline"
            

@method_decorator(JsonResponseDecorator, name='dispatch')
class UsernameAvailabilityView(View):

    def post(self, request):

        try:
            username   = request.POST.get('username')

        except KeyError:
            return invalid_params_response("Invalid parameters")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            print("Username available")
            return "available"

        print("Username unavailable")
        return "unavailable"
