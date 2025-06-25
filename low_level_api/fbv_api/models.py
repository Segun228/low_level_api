from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 100, editable=True)
    body = models.CharField(max_length= 100, blank= True)
    creation_date = models.DateField(auto_now_add= True)
    author = models.ForeignKey("RegularUser", on_delete=models.CASCADE, related_name="posts")
    images = models.JSONField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class RegularUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 100, editable=True, blank= False)
    email = models.EmailField(max_length= 100, blank= False)
    password = models.CharField(max_length= 100, blank= False)
    registration_date = models.DateField(auto_now_add= True)
    is_admin = models.BooleanField(default= False)
    def __str__(self):
        return self.username

