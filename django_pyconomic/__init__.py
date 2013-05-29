from django.conf import settings
from django.test.signals import setting_changed
from django.dispatch import receiver
from django.core.exceptions import ImproperlyConfigured
from pyconomic.client import Client
from pyconomic.mock_client import MockClient


client = None


def configure():
    """(Re-)configure pyconomic from the Django settings.

    :raises django.core.exceptions.ImproperlyConfigured:
        if one of the required settings are not set.
    """

    # Validate the application settings.
    for setting_name, setting_description in [
        ('PYCONOMIC_AGREEMENT_NUMBER', 'e-conomic agreement number', ),
        ('PYCONOMIC_USERNAME', 'e-conomic username', ),
        ('PYCONOMIC_PASSWORD', 'e-conomic password', ),
    ]:
        if hasattr(settings, setting_name):
            continue

        raise ImproperlyConfigured(
            'No %s configured for the application. Please set the `%s` '
            'setting' % (setting_description, setting_name)
        )

    # Instantiate the client.
    global client
    client_cls = MockClient if getattr(settings, 'PYCONOMIC_MOCK', False) \
        else Client
    client = client_cls(agreement_number=settings.PYCONOMIC_AGREEMENT_NUMBER,
                        username=settings.PYCONOMIC_USERNAME,
                        password=settings.PYCONOMIC_PASSWORD)


@receiver(setting_changed)
def setting_changed_callback(sender, **kwargs):
    """Reconfigure pyconomic when settings are changed during testing.
    """

    configure()


configure()


__all__ = ('client', )
