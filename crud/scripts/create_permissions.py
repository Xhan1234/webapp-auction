from crud.models import Product  # Replace with your actual model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import transaction  # Import transaction module

@transaction.atomic  # Use transaction.atomic to ensure all changes are saved or none
def run():
    # Define custom permissions with the correct codenames
    add_product_permission, _ = Permission.objects.get_or_create(
        codename='crud.add_product',
        name='Can add product',
        content_type=ContentType.objects.get_for_model(Product)
    )

    buy_product_permission, _ = Permission.objects.get_or_create(
        codename='crud.buy_product',
        name='Can buy product',
        content_type=ContentType.objects.get_for_model(Product)
    )

    # Assign permissions to groups as needed
    vendor_group = Group.objects.get(name='vendor')
    customer_group = Group.objects.get(name='customer')

    vendor_group.permissions.add(add_product_permission, buy_product_permission)
    customer_group.permissions.add(buy_product_permission)

if __name__ == "__main__":
    run()
