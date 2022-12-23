from django.contrib import admin
from Blog.models import Post, Profile


admin.site.register(Profile)
admin.site.register(Post)