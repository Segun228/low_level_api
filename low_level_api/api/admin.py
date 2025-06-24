from django.contrib import admin
from api.models import Post, RegularUser

admin.site.register(RegularUser)
admin.site.register(Post)