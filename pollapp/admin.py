from django.contrib import admin
from .models import Post, Comment, News, Poll
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Poll)