from django.apps import AppConfig


class NotepadAppConfig(AppConfig):

    name = "meeting_tool_backend.notepad"
    verbose_name = "Notepad"

    def ready(self):
        try:
            import url.signals  # noqa F401
        except ImportError:
            pass
