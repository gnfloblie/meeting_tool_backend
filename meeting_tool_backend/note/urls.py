from django.conf.urls import url
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "Note"
urlpatterns = [
    path('', view=csrf_exempt(views.NoteView.as_view()), name='note_view'),
    path('all/<int:notepad_id>', view=csrf_exempt(views.NoteView.as_view()), name='note_view'),
    path('single/', view=csrf_exempt(views.NoteSingleView.as_view()), name='note_singleview'),
]
