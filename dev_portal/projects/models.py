from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name