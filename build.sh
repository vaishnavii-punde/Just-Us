#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "============================================"
echo "👥 CREATING USERS"
echo "============================================"

python manage.py shell << 'HEREDOC'
from django.contrib.auth.models import User

# Admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin2025Pass!')
    print('✅ Created admin')
else:
    print('⚠️  admin already exists')

# Guddya user
if not User.objects.filter(username='Guddya').exists():
    User.objects.create_superuser('Guddya', 'guddya@example.com', 'ayush2727')
    print('✅ Created Guddya')
else:
    print('⚠️  guddya already exists')

# guddu user
if not User.objects.filter(username='guddu').exists():
    User.objects.create_superuser('guddu', 'guddu@example.com', 'ayush2727')
    print('✅ Created guddu')
else:
    print('⚠️  guddu already exists')

# Show all users
print(f'\n📊 Total users: {User.objects.count()}')
for user in User.objects.all():
    print(f'  - {user.username}')

HEREDOC

echo "============================================"
echo "✅ Build completed successfully!"
echo "============================================"