from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.forms.models import model_to_dict

from api.helpers.response_helpers import error_response, unauthorized_response
from api.helpers.user_helpers import *
from api.models import User
from api.decorators.response import JsonResponseDecorator


@method_decorator(JsonResponseDecorator, name='dispatch')
class LoginFormView(View):

    def post(self, request):
        """
        Authenticates and log in a valid user
        Disconnect with all the previous sessions of the user
        """
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('passToken'))
        
        if user is not None:
            remove_existing_sessions(user.user_id)
            request.session['user_id'] = user.user_id
            response = {
                'email'   : user.email,
                'username': user.username
            }
            return response
        else:
            try:
                user_obj = User.objects.get(email=request.POST.get('email'))
                return error_response("User password incorrect")
            except User.DoesNotExist:
                return error_response("User email incorrect")


@method_decorator(JsonResponseDecorator, name='dispatch')
class RegisterFormView(View):
    def post(self, request):
        """
        Check if the credentials are in proper format
        Check if the user with provided email already exits
        Register a user with default game data if it passes the above 2 test
        """
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        if validate_email(email) and len(password) >= 7 and username is not None:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email,
                                                username=username,
                                                password=password,
                                                status=False)
                # return "registration successful"
                return model_to_dict(user)
            else:
                return error_response("Email already exists")
        else:
            return error_response("Invalid user details")


@method_decorator(JsonResponseDecorator, name='dispatch')
class LogoutView(View):
    
    def post(self, request):
        """
        Logs out user
        Deletes his session
        """

        user = request.session.get('user_id')

        if user is not None:
            del request.session['user_id']
            return "Logged out successfully!"
        else:
            return error_response("Logout Error!")
