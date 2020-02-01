from django.apps import AppConfig
from django.conf import settings
from django.utils.module_loading import import_string
import sys



class DjkAppConfig(AppConfig):
    name = 'django_jinja_knockout'
    djk_middleware = None

    @classmethod
    def get_context_middleware(cls):
        if cls.djk_middleware is None:
            if hasattr(settings, 'DJK_MIDDLEWARE'):
                cls.djk_middleware = import_string(settings.DJK_MIDDLEWARE)
            else:
                if 'middleware' in dir() and 'middleware' not in sys.modules:
                    from . import middleware
                middleware.ContextMiddleware
        return cls.djk_middleware
