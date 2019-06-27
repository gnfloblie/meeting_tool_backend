from django.apps import AppConfig


class NoteAppConfig(AppConfig):

    name = "meeting_tool_backend.note"
    verbose_name = "Note"

    def ready(self):
        try:
            import url.signals  # noqa F401
        except ImportError:
            pass
