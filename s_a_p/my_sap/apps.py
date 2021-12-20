from django.apps import AppConfig
class MySapConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_sap"


class Home(AppConfig):
    default_auto_field = "home"
    name = "home"


class Client(AppConfig):
    default_auto_field = "client"
    name = "client"

class Resource(AppConfig):
    default_auto_field = "resource"
    name = "resource"

class Blog(AppConfig):
    default_auto_field = "blog"
    name = "blog"
