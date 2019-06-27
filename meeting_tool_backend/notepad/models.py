import datetime
from django.db import models
from meeting_tool_backend.participant.models import Participant
from meeting_tool_backend.users.models import User


class Notepad(models.Model):

    id = models.AutoField(primary_key=True)
    project_name = models.CharField(default='', max_length=30)
    title = models.CharField(default='', max_length=30)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(default='', max_length=30)
    participants = models.ManyToManyField(Participant, blank=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)

    @staticmethod
    def date_format(date):
        time_arr = []
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        time_arr.append(year)
        time_arr.append(month)
        time_arr.append(day)
        return time_arr

    @staticmethod
    def create_notepad(author):
        return Notepad.objects.create(
            author=author,
            project_name="",
            title="",
            location="",
        )

    @staticmethod
    def update_notepad(notepad, id):
        notepadObj = Notepad.objects.get(id=id)
        notepadObj.project_name = notepad.get("project_name")
        notepadObj.title = notepad.get("title")
        notepadObj.location = notepad.get("location")
        notepadObj.participants.set(notepad.get("participants"))
        notepadObj.save()
        return notepadObj

    @staticmethod
    def serialize_notepad(notepad):
        return {
            "id": notepad.id,
            "project_name": notepad.project_name,
            "title": notepad.title,
            "created_at": Notepad.date_format(notepad.created_at),
            "location": notepad.location,
            "participants": [Participant.serialize_participant(participant) for participant in notepad.participants.all()],
            "author": User.serialize_user(notepad.author)
        }
