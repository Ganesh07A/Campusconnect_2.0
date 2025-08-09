from django.db import models

class Council(models.Model):
    member_name = models.CharField(max_length=100)
    member_post = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='council_photos/', blank=True, null=True)

    def __str__(self):
        return self.member_name
