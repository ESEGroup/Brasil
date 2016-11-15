from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'people/$', views.people, name='people'),
    url(r'person/$', views.person, name='person'),
    url(r'catalog/$', views.catalog, name='catalog'),
    url(r'catalog/searchCatalog/$', views.searchCatalog, name='catalog'),
    url(r'catalog/newResource/createNewResource/$', views.createNewResource, name='create_new_resource'),
    url(r'catalog/newResource/$', views.newResource, name='new_resource'),
    url(r'catalog/(?P<id>-?[0-9]+)/$', views.resource, name='resource'),
]

urlpatterns += staticfiles_urlpatterns()
