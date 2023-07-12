# middleware.py

from django.contrib.auth.models import User


class CustomAdminContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/admin/'):
            # Get the existing context data from the response
            context = response.context_data

            # Add your custom context data to the dictionary
            
            context['user_count'] = User.objects.count()

            # Update the response with the modified context data
            response.context_data = context

        return response
