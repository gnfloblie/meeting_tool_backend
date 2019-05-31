from django.http import JsonResponse
from django.views.generic import DetailView
from .models import Note
from meeting_tool_backend.notepad.models import Notepad
import json


class NoteView(DetailView):

    def post(self, request):
        """
        POST /note/
        :param request:
        :return:
        """
        json_body = json.loads(request.body)
        id = json_body.get("id")
        note = Note.create_note(id)
        return JsonResponse(status=200, data={"result": Note.serialize_note(note)})

    def get(self, request, notepad_id=None):
        """
        GET /note/all/:notepad_id
        :param notepad_id:
        :return:
        """
        notes = Note.objects.filter(notepad=notepad_id)
        return JsonResponse(status=200, data={"result": [Note.serialize_note(note)
                                                             for note in notes]})

class NoteSingleView(DetailView):

    def put(self, request, id=None):
        """
        PUT note/single/:note_id
        :param id:
        :param request:
        :return:
        """
        required_fields = {}
        body = json.loads(request.body)
        if not body:
            return JsonResponse(status=400, data={"error": "Notiz existiert nicht!", "message": "Bearbeiten der Notiz fehlgeschlagen"})
        for field in required_fields:
            if field not in body:
                return JsonResponse(status=400, data={"error": "Feld fehlt", "message": "Bearbeiten der Notiz fehlgeschlagen"})
        updated_note = Note.update_note(body, id)
        return JsonResponse(status=200, data={"result": Note.serialize_note(updated_note)})
