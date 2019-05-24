import datetime
from django.db import models


class Note(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(default='', max_length=15)
    description = models.CharField(default='', max_length=100)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    content = models.CharField(default='', max_length=1000)

    @staticmethod
    def create_note():
        return Note.objects.create()

    @staticmethod
    def update_note(note, id):
        noteObj = Note.objects.get(id=id)
        noteObj.type = note.get("type")
        noteObj.description = note.get("description")
        noteObj.content = note.get("content")
        noteObj.save()
        return noteObj

    @staticmethod
    def serialize_note(note):
        return {
            "id": note.id,
            "type": note.type,
            "description": note.description,
            "created_at": note.created_at,
            "content": note.content
        }
