from django.db import models

class Comment(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        app_label = 'portfoilo'
