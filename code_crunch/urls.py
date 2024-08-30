from django.urls import path
from .views import *

urlpatterns = [
    path("display/<int:empID>/", displayEmailPageView, name="display"),
    path("displayAll/", DisplayAllPageView, name="displayAll"),
    # path("render/", RenderEmail, name="render"),
    path("", indexPageView, name="index")
]

#<str:targetPost>'