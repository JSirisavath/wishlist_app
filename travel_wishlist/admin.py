from django.contrib import admin
from .models import Place

# Be able to read, write, edit, etc the db by registering the db here.
# In addition to access those rights , you need to be admin, so run this on your terminal/console: ' python manage.py createsuperuser '
# After admin has been created in the terminal, navigate to the local host url and then put '/admin' after the url - then sign in
admin.site.register(Place)
