import datetime
from django.db import models
from meeting_tool_backend.note.models import Note
from meeting_tool_backend.participant.models import Participant


class Notepad(models.Model):

    id = models.AutoField(primary_key=True)
    project_name = models.CharField(default='', max_length=30)
    title = models.CharField(default='', max_length=30)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(default='', max_length=30)
    notes = models.ForeignKey(Note, blank=True, on_delete=models.CASCADE)
    participants = models.ForeignKey(Participant, blank=True, on_delete=models.CASCADE)

    @staticmethod
    def create_notepad():
        return Note.objects.create()

    @staticmethod
    def update_notepad(notepad, id):
        notepadObj = Notepad.objects.get(id=id)
        notepadObj.project_name = notepad.get("project_name")
        notepadObj.title = notepad.get("title")
        notepadObj.created_at = notepad.get("created_at")
        notepadObj.location = notepad.get("location")
        notepadObj.notes = notepad.get("notes")
        notepadObj.participants = notepad.get("participants")
        notepadObj.save()
        return notepadObj

    @staticmethod
    def serialize_notepad(notepad):
        return {
            "id": notepad.id,
            "project_name": notepad.project_name,
            "title": notepad.title,
            "created_at": notepad.created_at,
            "location": notepad.location,
            "notes": [Note.serialize_note(note) for note in notepad.notes.all()],
            "participants": [Participant.serialize_participant(participant) for participant in notepad.participant.all()]
        }
