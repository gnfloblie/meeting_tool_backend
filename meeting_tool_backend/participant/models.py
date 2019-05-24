import datetime
from django.db import models
from meeting_tool_backend.users.models import User


class Participant(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    anonymous = models.BooleanField(blank=True, default=False)


    @staticmethod
    def create_participant():
        return Participant.objects.create()

    @staticmethod
    def update_participant(participant, id):
        participantObj = Participant.objects.get(id=id)
        if participantObj.anonymous:
            participantObj.first_name = participant.get("first_name")
            participantObj.last_name = participant.get("last_name")
        else:
            participantObj.user = participant.get("user")
        participantObj.save()
        return participantObj

    @staticmethod
    def serialize_participant(participant):
        if participant.anonymous:
            return {
                "id": participant.id,
                "first_name": participant.first_name,
                "last_name": participant.last_name,
                "anonymous": participant.anonymous
            }
        else:
            return {
                "id": participant.id,
                "user": User.serialize_user(participant.user),
                "anonymous": participant.anonymous
            }
