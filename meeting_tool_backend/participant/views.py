from django.http import JsonResponse
from django.views.generic import DetailView
from meeting_tool_backend.notepad.models import Notepad
from .models import Participant
import json


class ParticipantView(DetailView):

    def post(self, request):
        """
        POST /participant/
        :param request:
        :return:
        """
        participant = json.loads(request.body)
        participant_obj = Participant.create_participant(participant)
        return JsonResponse(status=200, data={"result": Participant.serialize_participant(participant_obj)})

    def get(self, request):
        """
        GET /participant/
        :param request:
        :return:
        """
        participants = Participant.objects.all()
        return JsonResponse(status=200, data={"result": [Participant.serialize_participant(participant)
                                                             for participant in participants]})
