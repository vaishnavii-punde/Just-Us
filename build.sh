#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "============================================"
echo "👥 CREATING ADMIN USER - START"
echo "============================================"

python manage.py shell << 'HEREDOC'
from django.contrib.auth.models import User
import traceback

try:
    # Delete any existing admin
    User.objects.filter(username='admin').delete()
    print('🗑️  Deleted existing admin (if any)')
    
    # Create fresh admin
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='Admin2025Pass!'
    )
    print('✅ ✅ ✅ SUCCESSFULLY CREATED ADMIN USER ✅ ✅ ✅')
    print(f'Username: admin')
    print(f'Password: Admin2025Pass!')
    print(f'Email: admin@example.com')
    print(f'Is superuser: {admin_user.is_superuser}')
    print(f'Is staff: {admin_user.is_staff}')
    
except Exception as e:
    print('❌ ❌ ❌ ERROR CREATING ADMIN USER ❌ ❌ ❌')
    print(f'Error: {str(e)}')
    traceback.print_exc()

# Show all users
all_users = User.objects.all()
print(f'\n📊 Total users in database: {all_users.count()}')
for user in all_users:
    print(f'  - {user.username} (superuser: {user.is_superuser})')

HEREDOC

echo "============================================"
echo "👥 CREATING ADMIN USER - END"
echo "============================================"

echo "✅ Build completed successfully!"