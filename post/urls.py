from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path("index", postIndex),
    path("detail", postDetail),
    path("create", postCreate),
    path("delete", postDelete),
    path("update", postUpdate),
    path('detail/<int:id>',postDetail),


]