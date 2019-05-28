from django.http import JsonResponse
from django.views.generic import DetailView
from meeting_tool_backend.notepad.models import Notepad
from .models import Participant


class ParticipantView(DetailView):

    def post(self, request):
        """
        POST /participant/
        :param request:
        :return:
        """
        participant = json.loads(request.body)
        participantObj = Participant.create_participant(participant)
        return JsonResponse(status=200, data={"result": Participant.serialize_participant(participantObj)})
