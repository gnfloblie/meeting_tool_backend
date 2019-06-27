import datetime
from django.db import models
from meeting_tool_backend.users.models import User


class Participant(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    anonymous = models.BooleanField(blank=True, default=False)


    @staticmethod
    def create_participant(participant):
        if participant.get("anonymous"):
            return Participant.objects.create(
                first_name = participant.get("first_name"),
                last_name = participant.get("last_name"),
                anonymous = participant.get("anonymous")
        )
        else:
            user = User.objects.get(username = participant.get("username"))
            return Participant.objects.create(
                user = user,
                anonymous = participant.get("anonymous")
            )

    @staticmethod
    def serialize_participant(participant):
        if participant.anonymous == True:
            return {
                "id": participant.id,
                "first_name": participant.first_name,
                "last_name": participant.last_name,
                "anonymous": participant.anonymous
            }
        elif participant.anonymous == False:
            return {
                "id": participant.id,
                "user": User.serialize_user(participant.user),
                "anonymous": participant.anonymous
            }
