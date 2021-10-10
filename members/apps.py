from django.apps import AppConfig


class MembersConfig(AppConfig):
    name = 'members'

    #For the signals members.signal.create_profile
    def ready(self):
        import members.signals