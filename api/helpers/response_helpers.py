def invalid_params_response():
    '''
    defines the response sent out if the params are not valid
    '''

    response = {
        'status_code': 400,
        'data': 'Bad Request',
    }

    return response

def unauthorized_response():
    '''
    defines the response sent out if the request is unauthorized
    '''

    response = {
        'status_code': 401,
        'data': 'Unauthorized. User Credentials Incorrect.',
    }

    return response

def error_response(message):
    '''
    Used to generate error response with a message, when the requested
    action cannot be completed
    '''

    response = {
        'status_code': 400,
        'data': message,
    }

    return response
    