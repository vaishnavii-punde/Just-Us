#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "👥 Force creating admin user..."
python manage.py shell <<EOF
from django.contrib.auth.models import User

# Delete admin if exists, then recreate
User.objects.filter(username='admin').delete()

# Create fresh admin
User.objects.create_superuser('admin', 'admin@example.com', 'AdminPass2025!')
print('✅ FORCE CREATED admin user')
print('📝 Username: admin')
print('📝 Password: AdminPass2025!')
print(f'📊 Total users: {User.objects.count()}')
EOF

echo "✅ Build completed successfully!"