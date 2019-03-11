from django.contrib import admin
from .models import Post, Comment, News, Poll, Subscriber, SendNewsLetter
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Subscriber)
admin.site.register(SendNewsLetter)
@admin.register(Poll)

class PollAdmin(admin.ModelAdmin):
	readonly_fields = ['first_poll_count', 'second_poll_count']