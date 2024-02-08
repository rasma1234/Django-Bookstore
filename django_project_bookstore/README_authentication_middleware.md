**### Exercise: Authentication Middleware (Extend Bookstore Exercise)****#### Objective:**
Create a middleware that checks if a user is authenticated. If the user is not authenticated, they should be redirected to the login page.
Use this middleware for your  ***Bookstore*** .**#### Steps:**1.  ***Setting up the middleware*** :    Create a new Python file named `authentication_middleware.py` in one of your Django apps (e.g., `users` if you have one).    Inside this file, define the middleware class:

```
python
    from django.shortcuts import redirect

    class AuthenticationMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Code to be executed for each request before
            # the view (and later middleware) are called.

            response = ______
            if response:
                return response

            response = ____

            # Code to be executed for each request/response after
            # the view is called.

            return response


  
```

    This class-based middleware intercepts every request to check if the user is authenticated. If not, the user is redirected to the login page.2.***Register the middleware*** :    Open your project's `settings.py` file. Add the path to the `AuthenticationMiddleware` in the `MIDDLEWARE` setting. Make sure to place it after Django's `AuthenticationMiddleware`:

```
python
    MIDDLEWARE = [
        ...
      
        'your_app_name.authentication_middleware.AuthenticationMiddleware',
        ...
    ]
  
```

    Replace`your_app_name` with the name of your Django app where you created the middleware.4.  ***Testing*** :    Now, when you try to access any view while not being authenticated, you should be redirected to the login page.    - Logout if you're currently logged in.
    - Try accessing a page you know requires authentication.
    - You should be automatically redirected to the login page.** (bearbeitet) **
