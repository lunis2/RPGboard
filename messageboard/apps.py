from django.apps import AppConfig


class MesageboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messageboard'

    def ready(self):
        import messageboard.signals
