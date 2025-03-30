from django.core.management.base import BaseCommand
from api.models import User  # Adjust if your model is in a different app

class Command(BaseCommand):
    help = "Create default users for testing"

    def handle(self, *args, **kwargs):
        default_users = [
            {
                "email": "admin@example.com",
                "password": "admin123",
                "full_name": "Admin User",
                "phone_number": "9999999999",
                "role": "Admin",
            },
            {
                "email": "farmer@example.com",
                "password": "farmer123",
                "full_name": "Farmer John",
                "phone_number": "8888888888",
                "role": "Farmer",
            },
        ]

        for user_data in default_users:
            if not User.objects.filter(email=user_data["email"]).exists():
                user = User(
                    email=user_data["email"],
                    full_name=user_data["full_name"],  
                    phone_number=user_data["phone_number"],
                    role=user_data["role"],
                )
                user.set_password(user_data["password"])  # ✅ Hash password correctly
                user.save()
                
                self.stdout.write(self.style.SUCCESS(f"Created user: {user_data['email']}"))
            else:
                self.stdout.write(self.style.WARNING(f"User {user_data['email']} already exists"))
