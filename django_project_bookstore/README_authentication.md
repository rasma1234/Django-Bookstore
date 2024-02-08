*Django Authentication Exercise*
*Objective:*
To create a Django project where users can sign up, log in, and log out using Django's built-in authentication system. Extend the books store exercise from above.
 *Update Settings:*
    In settings.py:
    - add the redirects
 *Views for Authentication:*
 accounts/views.py; use  UserCreationForm
 *Templates:*
    Create templates for signup and login. Ensure you handle CSRF tokens and make use of Django's form handling.
 *URL Configuration:*
    create accounts/urls.py
    And include these URLs in the main urls.py:
python
    from django.urls import path, include

    urlpatterns = [
        path('account', include('django.contrib.auth.urls')),
        path('account', include('accounts.urls')),
    ]
    
 *Run Migrations:*
bash
    python manage.py migrate
    
 *Run the Server:*
bash
    python manage.py runserver
    
 *Test the Application:*
    Visit http://localhost:8000/accounts/signup/ to create a new account, http://localhost:8000/accounst/login/ to log in, and http://localhost:8000/accounts/logout/ to log out.