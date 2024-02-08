***Exercise 2: Django Rest Framework******Objective:*** Extend the `plantstore` project to include an API endpoint that lists all the plants in JSON format using DRF.1.  ***Setup*** :

- Install Django Rest Framework: `pip install djangorestframework`.
- Add `'rest_framework'` to `INSTALLED_APPS` in `plantstore`'s settings.2.  ***Serializers*** :
- In the `plants` app, create a serializer called `PlantSerializer` using DRF's `serializers.ModelSerializer`.
- This serializer should handle the `Plant` model.3.  ***API View*** :
- Create a DRF `ListAPIView` in `views.py` of the `plants` app that uses the `PlantSerializer` to display all the plants in the database in JSON format.
- Name this view as `PlantListAPI`.4.  ***URLs*** :
- In the `urls.py` of the `plants` app, add a URL pattern that maps to `PlantListAPI`.
- Make sure the API view is accessible at the path `/api/plants/`.5.  ***Testing*** :
- Access `/api/plants/` in your browser or through tools like `curl` or Postman.
- You should receive a JSON response with a list of plants.
