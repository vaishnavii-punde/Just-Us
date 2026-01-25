from django.db import migrations
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    """Create default users for Just-Us"""
    password = 'youarenotmyfriend2714' 
    
    if not User.objects.filter(username='Guddya').exists():
        User.objects.create_superuser(
            username='Guddya',
            email='guddya@example.com',
            password=password
        )
        print('✅ Created user: Guddya')
    else:
        print('⚠️  User Guddya already exists')
    
    if not User.objects.filter(username='guddu').exists():
        User.objects.create_superuser(
            username='guddu',
            email='guddu@example.com',
            password=password
        )
        print('✅ Created user: guddu')
    else:
        print('⚠️  User guddu already exists')
    
    print(f'📊 Total users: {User.objects.count()}')


def reverse_func(apps, schema_editor):
    User.objects.filter(username__in=['Guddya', 'guddu']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('lovehub', '0002_delete_lovenote'),
    ]

    operations = [
        migrations.RunPython(create_users, reverse_func),
    ]