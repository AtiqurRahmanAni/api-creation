from django.urls import path
from . views import *

urlpatterns = [
    path("parent/", ParentView.as_view(), name="parent"),
    path("child/", ChildView.as_view(), name="child"),
]
