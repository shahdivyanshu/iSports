from django.contrib import admin
from blogs.models import Post,Blogcomments

# Register your models here.
admin.site.register(Post)
admin.site.register(Blogcomments)
