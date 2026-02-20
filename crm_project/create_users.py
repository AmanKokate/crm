"""
Script to create test users for CRM system
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create Admin user
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@crm.com',
        'first_name': 'Admin',
        'last_name': 'User',
        'role': 'ADMIN',
        'is_staff': True,
        'is_superuser': True,
    }
)
if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print(f"✓ Admin user created: username=admin, password=admin123, role=ADMIN")
else:
    print(f"Admin user already exists: username=admin")

# Create Sales user
sales_user, created = User.objects.get_or_create(
    username='sales',
    defaults={
        'email': 'sales@crm.com',
        'first_name': 'Sales',
        'last_name': 'User',
        'role': 'SALES',
        'is_staff': False,
        'is_superuser': False,
    }
)
if created:
    sales_user.set_password('sales123')
    sales_user.save()
    print(f"✓ Sales user created: username=sales, password=sales123, role=SALES")
else:
    print(f"Sales user already exists: username=sales")

print("\n" + "="*60)
print("Test users are ready!")
print("="*60)
print("\nAdmin User:")
print("  Username: admin")
print("  Password: admin123")
print("  Role: ADMIN")
print("\nSales User:")
print("  Username: sales")
print("  Password: sales123")
print("  Role: SALES")
print("="*60)
