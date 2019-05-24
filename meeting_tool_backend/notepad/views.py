from django.http import JsonResponse
from django.views.generic import DetailView
from meeting_tool_backend.note.models import Note
from meeting_tool_backend.participant.models import Participant
from .models import Notepad
import json


class NotepadOverView(DetailView):

    def post(self, request):
        """
        POST /notepad/
        :param request:
        :return:
        """
        Notepad.created_at()
        return JsonResponse(status=200, data={"message": "Notizblock wurde hinzugefügt"})

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

    def put(self, request, notepad_id=None):
        """
        PUT notepad/:notepad_id
        :param notepad_id:
        :param request:
        :return:
        """
        required_fields = {project_name, title, location, notes, participants}
        body = json.loads(request.body)
        notepad = Notepad.obejcts.get(id=notepad_id)
        participants = []
        notes = []
        if not notepad:
            return JsonResponse(status=400, data={"error": "Notizblock existiert nicht!", "message": "Bearbeiten des Notizblockes fehlgeschlagen"})
        for field in required_fields:
            if field not in body:
                return JsonResponse(status=400, data={"error": "Feld fehlt", "message": "Bearbeiten des Notizblockes fehlgeschlagen"})
        for participant in body.participants:
            updated_participant = Participant.update_participant(participant)
            participants.append(updated_participant)
        body.participants = participants
        for note in body.notes:
            updated_note = Note.update_note(note)
            notes.append(updated_note)
        body.notes = notes
        updated_notepad = Notepad.update_notepad(body)
        return JsonResponse(status=200, data={"result": Notepad.serialize_notepad(updated_notepad)})
