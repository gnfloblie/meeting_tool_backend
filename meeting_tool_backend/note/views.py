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
        :param request:
        :param notepad_id:
        :return:
        """
        notes = Note.objects.filter(notepad=notepad_id)
        return JsonResponse(status=200, data={"result": [Note.serialize_note(note)
                                                             for note in notes]})

class NoteSingleView(DetailView):

    def put(self, request):
        """
        PUT note/single/
        :param request:
        :return:
        """
        body = json.loads(request.body)
        notes = []
        if not body:
            return JsonResponse(status=400, data={"error": "Notizen existieren nicht!", "message": "Bearbeiten der Notiz fehlgeschlagen"})
        for note in body:
            updated_note = Note.update_note(note, note.get('id'))
            notes.append(updated_note)
        return JsonResponse(status=200, data={"result": [Note.serialize_note(note)
                                                             for note in notes]})
