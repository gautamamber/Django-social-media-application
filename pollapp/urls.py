from . import views
from django.conf.urls import url, include
from django.contrib.auth.views import (login, logout)

from django.contrib.auth import views as auth_views
from django.urls import path
app_name = 'pollapp'
urlpatterns = [
	url(r'^login/$',login,{'template_name' : 'pollapp/login.html'}),
	url(r'^logout/$',logout, {'template_name' : 'pollapp/logout.html'}),
	url(r'^password/$', auth_views.PasswordChangeView.as_view(template_name='pollapp/password_change.html'),
        name='password_change'),
	url(r'^password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='pollapp/password_change_done.html'),
        name='password_change_done'),
	path('', views.post_list ,name = 'post_list'),
	path('<int:blog_id>/', views.details, name = "details"),
	# 
	path('register/', views.register, name = "register"),
	url(r'^like/$', views.like_post, name = "like_post"),
	path('news/', views.news, name = 'news'),
	path('about/', views.about, name = 'about'),
	path('former_minister/', views.chief_minister, name = 'chief_minister'),
	path('election_updates/', views.election_updates, name = 'election_updates'),
	path('news_letter/', views.send_newsletter, name = "news_letter"),
	path('election_update_details/<int:pk>', views.election_update_details, name = "election_update_details"),

	# url(r'^activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    
] 