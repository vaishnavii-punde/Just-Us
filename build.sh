#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "👥 Creating users..."
python manage.py shell <<EOF
from django.contrib.auth.models import User

password = 'youarenotmyfriend2714'

print('🔍 Checking for users...')
print(f'Current user count: {User.objects.count()}')

if not User.objects.filter(username='Guddya').exists():
    User.objects.create_superuser('Guddya', 'guddya@example.com', password)
    print('✅ Created user: Guddya')
else:
    print('⚠️  User Guddya already exists')

if not User.objects.filter(username='guddu').exists():
    User.objects.create_superuser('guddu', 'guddu@example.com', password)
    print('✅ Created user: guddu')
else:
    print('⚠️  User guddu already exists')

print(f'📊 Total users: {User.objects.count()}')
EOF

echo "✅ Build completed successfully!"