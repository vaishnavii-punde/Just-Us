import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justus.settings')
django.setup()

from django.contrib.auth.models import User

password = 'YourPassword123'  # Change this to your desired password

# Create Guddya
if not User.objects.filter(username='Guddya').exists():
    User.objects.create_superuser('Guddya', 'guddya@example.com', password)
    print('✅ Created user: Guddya')
else:
    print('⚠️  User Guddya already exists')

# Create guddu
if not User.objects.filter(username='guddu').exists():
    User.objects.create_superuser('guddu', 'guddu@example.com', password)
    print('✅ Created user: guddu')
else:
    print('⚠️  User guddu already exists')

print('🎉 Done!')