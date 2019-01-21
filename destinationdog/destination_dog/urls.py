from django.conf.urls import url
from destination_dog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'articles/$', views.article_list, name='article_list'),
    url(r'^articles/add_article/', views.add_article, name='add_article'),
    url(r'^articles/(?P<article_title_slug>[\w\-]+)/', views.show_article, name='show_article'),
    url(r'^dogofthemonth/$', views.dotm, name='dotm'),
    url(r'^dogofthemonth/vote/', views.dotm_vote, name='dotm_vote'),
    url(r'^dogofthemonth/enter/', views.dotm_enter, name='dotm_enter'),
    url(r'^dogofthemonth/hall_of_fame/', views.dotm_hall_of_fame, name='dotm_hall_of_fame'),
    url(r'^locateservice/$', views.locateServices, name='locateservice'),
    url(r'^locateservice/add_service/$', views.add_service, name='add_service'),
    url(r'^locateservice/(?P<service_name_slug>[\w\-]+)/', views.show_service, name='show_service'),
    url(r'^forum', views.forum, name='forum'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events/add_event/$', views.add_events, name='add_events'),
    url(r'^events/(?P<event_name_slug>[\w\-]+)/', views.show_event, name='show_event'),
    url(r'^about', views.about, name='about'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^sitemap', views.sitemap, name='sitemap'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^like/$', views.vote_dotm, name='vote_dotm'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='user_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/add_dog/$', views.add_dog, name='add_dog'),
    url(r'^dogprofile/(?P<dog_name_slug>[\w\-]+)/', views.dogprofile, name='dogprofile'),
    url(r'^deactivate/$', views.deactivate_profile, name="deactivate")

]
