from time import timezone
from django.db import models
from uuid import uuid4

# partially borrowed from: https://python.plainenglish.io/how-to-create-a-django-image-gallery-website-in-2-hours-bdb42464fbfe
# with modifications (no category)

class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)

    # FrontPage flag - controls if it's a frontpage image or just in the gallery
    # TODO: consider adding more categories?  Would be an interesting dropdown from the top-nav
    showOnFrontPage = models.BooleanField(blank=False, null=False, default=False)

    # Utilities
    uniqueId = models.CharField(null=True, blank=True, max_length=100, default=timezone.now())
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now())

    imageSource = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.uniqueId

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        super(Image, self).save(*args, **kwargs)
