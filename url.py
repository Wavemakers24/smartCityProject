from django.conf.urls import url
from . import views

app_name = 'smartcity'

urlpatterns = [
    #/smartcity/
    #url(r'^userlist/$', views.index, name= 'index'),

    #/smartcity/register/
    #url(r'^register/$', views.register, name= 'register'),

    #/smartcity/userprofile123/(?P<UserID>[0-9]+)
    url(r'^userlist/(?P<user_id>[0-9]+)/$', views.userprofile, name= 'userprofile'),

    #/smartcity/userlist/123/editonfo/
    url(r'^userlist/(?P<user_id>[0-9]+)/editinfo/$', views.editinfo, name= 'editinfo'),

    url(r'^$', views.welcome, name='index'),
    url(r'^register$', views.registerView.as_view(), name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^template$', views.template, name='template'),
    url(r'^account$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),

]