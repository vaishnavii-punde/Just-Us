#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "👥 Creating admin superuser (if not exists)..."
python manage.py shell <<EOF
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'AdminPass2025!')
    print('✅ Created admin user')
    print('📝 Login at /admin/ with username: admin, password: AdminPass2025!')
else:
    print('⚠️  Admin user already exists')

print(f'📊 Total users in database: {User.objects.count()}')
print('ℹ️  Create Guddya and guddu users manually at /admin/')
EOF

echo "✅ Build completed successfully!"