from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255,null=False)
    subtitle = models.CharField(max_length=255,null=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
