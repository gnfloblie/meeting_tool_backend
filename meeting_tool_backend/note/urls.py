from django.conf.urls import url
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "Note"
urlpatterns = [
    path('', view=csrf_exempt(views.NoteView.as_view()), name='note_view'),
    path('<int:id>', view=csrf_exempt(views.NoteView.as_view()), name='note_view'),
]
