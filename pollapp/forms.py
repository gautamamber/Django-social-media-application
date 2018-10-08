from django import forms
from .models import Comment
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	
	# exmaple photo class : resolution pixel or info about model
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'email','password1', 'password2',]:
			self.fields[fieldname].help_text = None
	

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email = email)
		if r.count():
			raise ValidationError("Email already exixts")
		return email

	class Meta:
		model = User

		fields = ('username', 'first_name' , 'last_name','email', 'password1', 'password2')

	def save(self,commit = True):
		user =  super(RegistrationForm, self).save(commit = False)
		user.first_name =  self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class CommentForm(forms.ModelForm):
	content = forms.CharField(label = "" , widget = forms.Textarea(attrs = {'class' :'form-control' , 'placeholder' : 'Text goes here!!!' , 'rows':'4' , 'cols' : '50'}))
	class Meta:
		model = Comment
		fields = {'content',}