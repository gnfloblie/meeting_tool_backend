from django.http import JsonResponse
from django.views.generic import DetailView
from meeting_tool_backend.notepad.models import Notepad
from .models import Participant


class ParticipantView(DetailView):

    def post(self, request, notepad_id=None):
        """
        POST /participant/
        :param notepad_id:
        :param request:
        :return:
        """
        participant = Participant.create_participant()
        notepad = Notepad.object.get(id=notepad_id)
        notepad.participants.append(participant)
        return JsonResponse(status=200, data={"message": "Teilnehmer wurde zum Notizblock hinzugefügt"})
