from django.conf.urls import url
from . import views
# the period means: form this current directory we are in, we looking ofr a dircetory called views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
]
