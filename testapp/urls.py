from django.urls import path
from .views import *

urlpatterns = [
    path("home",hme,name="home"),
    path("contact",cont,name="contact"),
    path("about",Abou,name="about"),
    path("service",services,name="sevices"),
    path("path-test",Path,name="path"),
    path("path-testing",TestImgTwo,name="path-testing")

]