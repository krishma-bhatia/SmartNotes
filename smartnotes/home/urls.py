from django.urls import path

from . import views


urlpatterns = [
    #path('home',views.home),
    #path('authorised',views.authorised),
    #Changing for class based views
    path("home",views.HomeView.as_view()),
    path("authorised",views.AuthorisedView.as_view()),
]