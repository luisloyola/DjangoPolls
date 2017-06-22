from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	#Generic views uses <pk>

    # ex: /polls/
    #url(r'^$', views.index, name='index'), #Classic view
 	url(r'^$', views.IndexView.as_view(), name='index'), #Generic view
    
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), #Generic view
    
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
 	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), #Generic view

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
