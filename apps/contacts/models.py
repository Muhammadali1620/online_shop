from django.db import models
from apps.general.servises import normalize_text
from apps.users.models import CustomUser

 
class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.title}'
    
    def get_normalize_fields(self):
        return ['name', 'title', 'message']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
