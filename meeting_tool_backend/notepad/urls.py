from django.conf.urls import url
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "Notepad"
urlpatterns = [
    path('', view=csrf_exempt(views.NotepadOverView.as_view()), name='notepad_overview'),
    path('all/<int:user_id>', view=csrf_exempt(views.NotepadOverView.as_view()), name='notepad_overview'),
    path('single/<int:id>', view=csrf_exempt(views.NotepadSingleView.as_view()), name='notepad_singleview'),
]
