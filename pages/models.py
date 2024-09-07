from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    mailSent = models.BooleanField(default=False)
    def __str__(self):
        return self.name