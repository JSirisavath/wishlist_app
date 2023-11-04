from django.db import models


# What does 'Place' contain? Create a class for this using models(DB) inside the class - this will talk to the database and map out what is in the 'Place' class
class Place(models.Model):
    # Map our Columns for Place:
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited? {self.visited}'

# After defining the Place class for models, we  need to set up the migrations (create/modifying an instructions on how to create DB table to handle this information) to do so, run 'python manage.py makemigrations' and run 'python manage.py migrate' to ask the db to create that table
