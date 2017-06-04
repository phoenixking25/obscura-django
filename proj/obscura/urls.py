from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', views.entry, name = 'entry'), 
	url(r'^home/$', views.index, name = 'index'),
	url(r'^about/$', views.about, name = 'about'),
	url(r'^team/$', views.team, name = 'team'),
	url(r'^auth/login/$',views.login_view,name='login_view'),
	url(r'^info/(?P<pk>\d+)/$', views.get_info, name = 'get_info'),
	url(r'^level/$', views.levelview, name  = 'levelview'),
    url(r'^auth/register/$',views.register_view,name='register_view'),
    url(r'^auth/logout/$',views.logout_view,name='logout_view'),

]