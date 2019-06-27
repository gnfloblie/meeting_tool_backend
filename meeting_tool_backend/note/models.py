import datetime
from django.db import models
from meeting_tool_backend.notepad.models import Notepad


class Note(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(default='', max_length=15)
    description = models.CharField(default='', max_length=100)
    due = models.DateTimeField(null=True, blank=True)
    content = models.CharField(default='', max_length=1000)
    notepad = models.ForeignKey(Notepad, blank=True, on_delete=models.CASCADE, null=True)

    @staticmethod
    def create_note(notepad_id):
        notepad = Notepad.objects.get(id=notepad_id)
        return Note.objects.create(
            type="",
            description="",
            content="",
            notepad=notepad
        )

    @staticmethod
    def update_note(note, id):
        noteObj = Note.objects.get(id=id)
        noteObj.type = note.get("type")
        noteObj.description = note.get("description")
        noteObj.due = note.get("due")
        noteObj.content = note.get("content")
        noteObj.save()
        return noteObj

    @staticmethod
    def serialize_note(note):
        return {
            "id": note.id,
            "type": note.type,
            "description": note.description,
            "due": note.due,
            "content": note.content,
            "notepad": Notepad.serialize_notepad(note.notepad)
        }
