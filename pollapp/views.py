from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, News
from .forms import RegistrationForm, CommentForm
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def about(request):
	return render(request, 'pollapp/about.html')

def election_updates(request):
	return render(request, 'pollapp/election_updates.html')

def former_minister(request):
	return render(request, 'pollapp/former_minister.html')

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
	return render(request, 'pollapp/post_list.html',  {'posts' : posts})




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
			# content = request.POST.get('content')
			# reply_id = request.POST.get('comment_id')
			# comment_qs = None
			# if reply_id:
			# 	comment_qs = Comment.objects.get(id = reply_id)
			# comment = Comment.objects.get_or_create(post = posts ,reply = None, user = request.user , content = content)
			# comment.save()
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
def polls_between_two(request):
	return render(request, "pollapp/polls.html")