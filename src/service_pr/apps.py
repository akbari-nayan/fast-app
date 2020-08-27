from django.apps import AppConfig


class ServicePrConfig(AppConfig):
    name = 'service_pr'

    def ready(self):
        import service_pr.signals