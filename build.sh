#!/usr/bin/env bash
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running database migrations..."
python manage.py migrate

echo "============================================"
echo "👥 CHECKING/CREATING ADMIN USER"
echo "============================================"

python manage.py shell << 'HEREDOC'
from django.contrib.auth.models import User

try:
    # Check if admin exists
    if User.objects.filter(username='admin').exists():
        print('⚠️  Admin user already exists - KEEPING IT')
        admin_user = User.objects.get(username='admin')
        print(f'   Username: {admin_user.username}')
        print(f'   Is superuser: {admin_user.is_superuser}')
    else:
        # Create admin only if it doesn't exist
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='Admin2025Pass!'
        )
        print('✅ SUCCESSFULLY CREATED ADMIN USER')
        print(f'   Username: admin')
        print(f'   Password: Admin2025Pass!')
    
    # Show all users
    all_users = User.objects.all()
    print(f'\n📊 Total users in database: {all_users.count()}')
    for user in all_users:
        print(f'  - {user.username} (superuser: {user.is_superuser})')
    
    print('\nℹ️  Create Guddya and guddu via /admin/ if they don\'t exist')
    
except Exception as e:
    print(f'❌ ERROR: {str(e)}')

HEREDOC

echo "============================================"
echo "✅ Build completed successfully!"
echo "============================================"