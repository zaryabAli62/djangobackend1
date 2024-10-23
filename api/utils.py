from functools import wraps
from django.http import JsonResponse
import jwt
from django.conf import settings

def token_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        # Get the Authorization header
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        # Ensure the Authorization header contains a Bearer token
        if not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Invalid token scheme, expected Bearer'}, status=401)

        # Extract the token
        token = auth_header.split(' ')[1]

        try:
            # Decode the token and validate it
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            # Optionally add user info to the request
            request.user_payload = payload
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # If token is valid, proceed to the view
        return f(request, *args, **kwargs)
    
    return decorated_function
