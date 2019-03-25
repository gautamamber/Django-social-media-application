from django.contrib import admin
from .models import Post, Comment, News, Subscriber, SendNewsLetter
from django.core.mail import send_mail

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Subscriber)


@admin.register(SendNewsLetter)
class SendNewsLetterAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		all_subscriber = Subscriber.objects.all()	
		email = []
		try:
			for i in all_subscriber:
				email.append(i.email)
			complete_mail = obj.title + "\n" + obj.text + "\n" + obj.links
			send_mail(obj.title, complete_mail, 'gautamamber5@gmail.com', email)
			super().save_model(request, obj, form, change)
		except:
			print("Sorry somethinh wrong")
