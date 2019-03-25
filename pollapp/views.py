from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, News, Subscriber
from .forms import RegistrationForm, CommentForm, NewsForm, NewsLetterForm
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
# Create your views here.

def about(request):
	return render(request, 'pollapp/about.html')

def election_updates(request):
	return render(request, 'pollapp/election_updates.html')

def former_minister(request):
	return render(request, 'pollapp/chief_minister.html')

def news(request):
	new = News.objects.all()
	context = {
	'new' : new
		}
	return render(request, 'pollapp/news.html',  context)


@login_required
def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	context = {
	'posts' : posts
	}
	if request.method == 'POST':
		form = NewsForm(request.POST or None)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			email_save = Subscriber(email = email)
			email_save.save()
			return redirect('/nirvachit')
	else:
		form = NewsForm()
	return render(request, 'pollapp/post_list.html',  {'posts' : posts, 'form':form})


@login_required
def details(request, blog_id):
	posts = get_object_or_404(Post, pk = blog_id)
	comments = Comment.objects.filter(post__title = posts)
	is_liked = False
	if posts.likes.filter(id = request.user.id).exists():
		is_liked = True

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = comment_form.cleaned_data.get('content')
			comment = Comment(user = request.user, content = content, post  = posts )
			comment.save()
			return HttpResponseRedirect(posts.get_absolute_url())
	else:
		comment_form = CommentForm()	
		context = {'posts' : posts, 'is_liked' : is_liked, 'total_likes' : posts.total_likes, 'comments' : comments, 'comment_form' : comment_form}
	return render(request, 'pollapp/details.html' , context )



@login_required
def like_post(request):
	posts = get_object_or_404(Post, id = request.POST.get('post_id'))
	is_liked = False
	if posts.likes.filter(id = request.user.id).exists():
		posts.likes.remove(request.user)
		is_liked = False
	else:
		posts.likes.add(request.user)
		is_liked = True
	# posts.likes.add(request.user)
	return HttpResponseRedirect(posts.get_absolute_url())

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/nirvachit/login/')
	else:
		form = RegistrationForm
	args = {'form' : form}
	return render(request, 'pollapp/reg_forms.html', args)


@login_required
def send_newsletter(request):
	if request.user.is_staff:
		if request.method == "POST":
			form = NewsLetterForm(request.POST)
			try:
				if form.is_valid():
					post = form.save(commit=False)
					all_subscriber = Subscriber.objects.all()	
					email = []
					for i in all_subscriber:
						email.append(i.email)
					complete_mail = post.title + "\n" + post.text + "\n" + post.links
					send_mail(post.title, complete_mail, 'gautamamber5@gmail.com', email)
					post.save()
					return redirect('/nirvachit/')
			except:
				print("Sorry something went wrong")
		else:
			form = NewsLetterForm()
		return render(request, "pollapp/news_letter.html", {"form":form})
	else:
		return render(request, "pollapp/no_news_letter.html")





