import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justus.settings')
django.setup()


from django.db import migrations
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    """Create default users for Just-Us"""
    password = 'keepitsame'  
    
    # Create Guddya
    if not User.objects.filter(username='Guddya').exists():
        User.objects.create_superuser(
            username='Guddya',
            email='guddya@example.com',
            password=password
        )
        print('✅ Created user: Guddya')
    
    # Create guddu
    if not User.objects.filter(username='guddu').exists():
        User.objects.create_superuser(
            username='guddu',
            email='guddu@example.com',
            password=password
        )
        print('✅ Created user: guddu')


def remove_users(apps, schema_editor):
    """Remove users if migration is reversed"""
    User.objects.filter(username__in=['Guddya', 'guddu']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('lovehub', '0003_create_default_users.py'),  # Change this to your last migration
    ]

    operations = [
        migrations.RunPython(create_users, remove_users),
    ]