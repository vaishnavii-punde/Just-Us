#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "============================================"
echo "👥 CREATING ALL USERS"
echo "============================================"

python manage.py shell << 'HEREDOC'
from django.contrib.auth.models import User

try:
    # Create admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin2025Pass!')
        print('✅ Created admin')
    else:
        print('⚠️  admin already exists')

    # Create guddya
    if not User.objects.filter(username='guddya').exists():
        User.objects.create_superuser('guddya', 'guddya@example.com', 'ayush2727')
        print('✅ Created Guddya')
    else:
        print('⚠️  guddya already exists')

    # Create guddu
    if not User.objects.filter(username='guddu').exists():
        User.objects.create_superuser('guddu', 'guddu@example.com', 'ayush2727')
        print('✅ Created guddu')
    else:
        print('⚠️  guddu already exists')

    # Show all users
    all_users = User.objects.all()
    print(f'\n📊 Total users in database: {all_users.count()}')
    for user in all_users:
        print(f'  - {user.username} (superuser: {user.is_superuser})')
    
except Exception as e:
    print(f'❌ ERROR: {str(e)}')

HEREDOC

echo "============================================"
echo "✅ Build completed successfully!"
echo "============================================"