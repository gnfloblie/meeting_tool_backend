from django.http import JsonResponse
from django.views.generic import DetailView
from meeting_tool_backend.note.models import Note
from meeting_tool_backend.participant.models import Participant
from meeting_tool_backend.users.models import User
from .models import Notepad
import json


class NotepadOverView(DetailView):

    def post(self, request):
        """
        POST /notepad/
        :param request:
        :return:
        """
        participants = []
        json_body = json.loads(request.body)
        author = User.objects.get(username=json_body.get("username"))
        participant = Participant.objects.get(user_id=author.id)
        participants.append(participant)
        notepad = Notepad.create_notepad(author)
        notepad.participants.set(participants)
        notepad.save()
        note = Note.create_note(notepad.id)
        return JsonResponse(status=200, data={"notepad": Notepad.serialize_notepad(notepad),
                                              "note": Note.serialize_note(note)
                                              })

    def get(self, request, user_id=None):
        """
        GET /notepad/:user_id
        :param request:
        :param user_id:
        :return:
        """
        notepads = Notepad.objects.filter(author=user_id)
        return JsonResponse(status=200, data={"result": [Notepad.serialize_notepad(notepad)
                                                             for notepad in notepads]})


class NotepadSingleView(DetailView):

    def get(self, request, id=None):
        """
        GET notepad/:id
        :param request:
        :param id:
        :return:
        """
        notepad = Notepad.objects.get(id=id)
        return JsonResponse(status=200, data={"result": Notepad.serialize_notepad(notepad)})

    def put(self, request, id=None):
        """
        PUT notepad/:id
        :param id:
        :param request:
        :return:
        """
        required_fields = {}
        body = json.loads(request.body)
        notepad = Notepad.objects.get(id=id)
        participants = []
        if not notepad:
            return JsonResponse(status=400, data={"error": "Notizblock existiert nicht!", "message": "Bearbeiten des Notizblockes fehlgeschlagen"})
        for field in required_fields:
            if field not in body:
                return JsonResponse(status=400, data={"error": "Feld fehlt", "message": "Bearbeiten des Notizblockes fehlgeschlagen"})
        if body.get("newParticipants") != []:
            for y in range(0, len(body.get("newParticipants")) - 1, 2):
                participant = {
                    'first_name': body.get("newParticipants")[y]
                }
                y += 1
                participant = {
                    'first_name': participant.get("first_name"),
                    'last_name': body.get("newParticipants")[y],
                    'anonymous': True
                }

                created_participant = Participant.create_participant(participant)
                participants.append(created_participant)
        for participant in body.get("participants"):
            participants.append(Participant.objects.get(id=participant.get('item_id')))
        del body.get("participants")[:]
        for participant in participants:
            body.get("participants").append(participant)
        updated_notepad = Notepad.update_notepad(body, id)
        return JsonResponse(status=200, data={"result": Notepad.serialize_notepad(updated_notepad)})
