from pyexpat import model
from re import template
from django.shortcuts import render
from .models import Notes
from django.views.generic import DetailView, ListView
#from django.http import Http404

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name='notes/detail.html'


# Create your views here.
# def list(request):
#     notes_list= Notes.objects.all()
#     return render(request,'notes/list.html',{'notes': notes_list})

# def detail(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request,'notes/detail.html',{'note': note})