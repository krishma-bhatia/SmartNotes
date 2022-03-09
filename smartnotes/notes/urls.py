from django.urls import path

from . import views

urlpatterns = [
    #For functional views
    # path("notes",views.list),
    # path("notes/<int:pk>",views.detail),
    # For Class based View
    path("notes/",views.NotesListView.as_view()),
    path("notes/<int:pk>",views.NotesDetailView.as_view())
]