from django.apps import AppConfig


class ParticipantAppConfig(AppConfig):

    name = "meeting_tool_backend.participant"
    verbose_name = "Participant"

    def ready(self):
        try:
            import url.signals  # noqa F401
        except ImportError:
            pass
