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
        json_body = json.loads(request.body)
        author = User.objects.get(username=json_body.get("username"))
        notepad = Notepad.create_notepad(author)
        note = Note.create_note(notepad.id)
        return JsonResponse(status=200, data={"notepad": Notepad.serialize_notepad(notepad),
                                              "note": Note.serialize_note(note)
                                              })

    def get(self, request):
        """
        GET /notepad/
        :param request:
        :return:
        """
        notepads = Notepad.objects.all()
        return JsonResponse(status=200, data={"result": [Notepad.serialize_notepad(notepad)
                                                             for notepad in notepads]})


class NotepadSingleView(DetailView):

    def get(self, request, notepad_id=None):
        """
        GET notepad/:notepad_id
        :param request:
        :param notepad_id:
        :return:
        """
        notepad = Notepad.objects.get(id=notepad_id)
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
        for participant in body.get("participants"):
            if participant.get("anonymous"):
                if participant.get("existing"):
                    anonymous_participant = Participant.objects.get(id=participant.get("id"))
                    participants.append(anonymous_participant)
                else:
                    new_participant = Participant.create_participant(participant)
                    participants.append(new_participant)
            else:
                if participant.get("existing"):
                    user = User.objects.get(username=participant.get("name"))
                    print(user)
                    participant_obj = Participant.objects.get(user=user.id)
                    print(participant_obj)
                    participants.append(participant_obj)
                else:
                    new_participant = Participant.create_participant(participant)
                    print(new_participant)
                    participants.append(new_participant)
        del body.get("participants")[:]
        print(participants)
        for participant in participants:
            body.get("participants").append(participant)
        updated_notepad = Notepad.update_notepad(body, id)
        return JsonResponse(status=200, data={"result": Notepad.serialize_notepad(updated_notepad)})
