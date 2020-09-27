from django.apps import AppConfig


class OnlineConfig(AppConfig):
    name = 'online'

    def ready(self):
        import online.signals
