from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "transactions"

#un fichier pour definir les carateristiques de base de l'application et les models qu'elle contient