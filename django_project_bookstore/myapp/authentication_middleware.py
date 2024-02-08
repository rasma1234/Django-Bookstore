from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_authenticated and request.path != reverse('login') and request.path != reverse('signup'):
            return HttpResponseRedirect(reverse('login'))  
                
        response = self.get_response(request)
        return response

# from django.shortcuts import redirect
# from django.urls import reverse

# class AuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not request.user.is_authenticated:
#             if request.path != reverse('login') and request.path != reverse('signup'):
#                 return redirect('login')
#         response = self.get_response(request)
#         return response
