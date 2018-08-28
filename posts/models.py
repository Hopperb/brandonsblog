from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    content = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
   

class PersonalPost(Post):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)