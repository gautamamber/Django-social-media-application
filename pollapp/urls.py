from . import views
from django.conf.urls import url, include
from django.contrib.auth.views import (login, logout, password_reset, password_reset_done, password_reset_confirm,
password_reset_complete)
from django.urls import path
app_name = 'pollapp'
urlpatterns = [
	url(r'^login/$',login,{'template_name' : 'pollapp/login.html'}),
	url(r'^logout/$',logout, {'template_name' : 'pollapp/logout.html'}),
	path('', views.post_list ,name = 'post_list'),
	path('<int:blog_id>/', views.details, name = "details"),
	# 
	path('register/', views.register, name = "register"),
	url(r'^like/$', views.like_post, name = "like_post"),
	path('news/', views.news, name = 'news'),
	path('about/', views.about, name = 'about'),
	path('former_minister/', views.former_minister, name = 'former_minister'),
	path('election_updates/', views.election_updates, name = 'election_updates'),
	path('news_letter/', views.send_newsletter, name = "news_letter"),

	# url(r'^activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    
] 