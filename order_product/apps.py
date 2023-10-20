from django.apps import AppConfig


class OrderProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_product'

class OrderProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_product'

    def ready(self):
        import order_product.signals  # Import the signals module