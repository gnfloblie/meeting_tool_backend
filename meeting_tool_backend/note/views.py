from django.http import JsonResponse
from django.views.generic import DetailView
from .models import Note
from meeting_tool_backend.notepad.models import Notepad


class NoteView(DetailView):

    def post(self, request, notepad_id=None):
        """
        POST /note/
        :param notepad_id:
        :param request:
        :return:
        """
        note = Note.create_note()
        notepad = Notepad.object.get(id=notepad_id)
        notepad.notes.append(note)
        return JsonResponse(status=200, data={"message": "Notiz wurde zum Notizblock hinzugefügt"})
