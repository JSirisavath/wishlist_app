from django.db import models

from django.contrib.auth.models import User

from django.core.files.storage import default_storage

# What does 'Place' contain? Create a class for this using models(DB) inside the class - this will talk to the database and map out what is in the 'Place' class


class Place(models.Model):
    # Map our Columns for Place:

    # Foreign Key is built in with Django models
    # User cannot be null
    # on_delete is a method/argument from django or the value for user deletion will be delete all places associated with that user
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    # Text field allows for unlimited entries, charField is limited of how much text you can put in
    # Notes can be optional
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    # The ImageField has a upload_to url string to models database.
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def save(self, *arg, **kwargs):
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            # If the older photo is different from the new photo, then delete that old photo and then replace it with that new photo
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)

        # Call super class method save, for generic saving POST objects
        super().save(*arg, **kwargs)

    def delete_photo(self, photo):
        # check if that photo exists first before deleting it
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    # When the place is deleted, delete the picture completely as well.

    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)

        super().delete(*args, **kwargs)

    def __str__(self):
        # A photo url will be generated if there is a photo else it will display 'no photo' string to the models, or it will be sent for rendering
        photo_str = self.photo.url if self.photo else 'no photo'
        # Truncate the first 100 characters for notes
        notes_str = self.notes[100:] if self.notes else 'no notes'
        return f'{self.name} visited? {self.visited}. Notes: {notes_str}. Photo {photo_str}'

# After defining the Place class for models, we  need to set up the migrations (create/modifying an instructions on how to create DB table to handle this information) to do so, run 'python manage.py makemigrations' and run 'python manage.py migrate' to ask the db to create that table
