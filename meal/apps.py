from django.apps import AppConfig


class MealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meal'

    def ready(self) -> None:
        import meal.signal
        return super().ready()
