from django.conf.urls import url
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "Participant"
urlpatterns = [
    path('', view=csrf_exempt(views.ParticipantView.as_view()), name='participant_view'),
]
