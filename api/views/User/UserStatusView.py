from django.views import generic
from django.views.generic import View
from django.utils.decorators import method_decorator

from api.models import User, Course
from api.helpers.response_helpers import error_response, invalid_params_response
from api.decorators.response import JsonResponseDecorator

@method_decorator(JsonResponseDecorator, name='dispatch')
class GetOnlineView(View):

    def post(self, request):
        
        try:
            username   = request.POST.get('username')
            token      = request.POST.get('token')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')

        except KeyError:
            return invalid_params_response("Invalid parameters")

        status       = True
        online_users = []

        users = Course.objects.values('username__username', 'platform','coursename').filter(platform=platform, coursename=coursename, status=status).exclude(username=username)

        for user in users:
            online_users.append({
                'username'   : user['username__username'],
                'platform'   : user['platform'],
                'coursename' : user['coursename']
            })

        return online_users


@method_decorator(JsonResponseDecorator, name='dispatch')
class PutOnlineView(View):
    
    def post(self, request):

        try:
            username   = request.POST.get('username')
            token      = request.POST.get('token')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')  
            status     = True

        except KeyError:
            return invalid_params_response("Invalid parameters")

        course = ""
        user   = ""

        try:
            user = User.objects.get(username=username, token=token)

        except User.DoesNotExist:
            user = User.objects.create(username=username, token=token)
            print("User created")

        try:
            course = Course.objects.get(username=user, platform=platform, coursename=coursename)

        except Course.DoesNotExist:

            if user is not None:
                course = Course.objects.create(username=user, platform=platform, coursename=coursename, status=status)
                print("User course created and status made online")
                return "User course created and status made online"           

        if course is not None:
            course.status = status
            course.save()
            print("User status made online")
            return "User status made online"
            

@method_decorator(JsonResponseDecorator, name='dispatch')
class PutOfflineView(View):
    
    def post(self, request):
    
        try:
            username   = request.POST.get('username')
            token      = request.POST.get('token')
            platform   = request.POST.get('platform')
            coursename = request.POST.get('coursename')  
            status     = False

        except KeyError:
            return invalid_params_response("Invalid parameters")

        course = ""
        user   = ""
        
        try:
            user = User.objects.get(username=username, token=token)

        except User.DoesNotExist:
            user = User.objects.create(username=username, token=token)
            print("User created")

        try:
            course = Course.objects.get(username=user, platform=platform, coursename=coursename)

        except Course.DoesNotExist:

            if user is not None:
                course = Course.objects.create(username=user, platform=platform, coursename=coursename, status=status)
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
