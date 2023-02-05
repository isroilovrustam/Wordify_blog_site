from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
