from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.files import File
import qrcode
from io import BytesIO
import json

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password=None, role='Customer'):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, phone_number=phone_number, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, password):
        user = self.create_user(email, full_name, phone_number, password, role='Admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('Farmer', 'Farmer'),
        ('Customer', 'Customer'),
        ('Admin', 'Admin'),
        ('Verifier', 'Verifier'),
        ('HerbalExpert', 'Herbal Expert'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='Customer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.email
        groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="api_user_groups",  # Custom related_name
        related_query_name="api_user",
    )
    # Add these custom permission fields at the end of your model:
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",  # Changed
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  
        related_query_name="custom_user",
    )

    objects = UserManager()

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    farm_area = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    expertise = models.CharField(max_length=50, choices=[
        ('Crops', 'Food Crops'),
        ('Herbs', 'Medicinal Herbs'),
        ('Both', 'Both')
    ], default='Crops')

    def __str__(self):
        return f"{self.user.full_name}'s Farm"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    interests = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user.email}'s Profile"

class CertificationRequest(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    submitted_documents = models.FileField(upload_to='certification_documents/')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    submitted_at = models.DateTimeField(default=timezone.now)
    inspection_date = models.DateField(null=True, blank=True)
    approval_date = models.DateField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True, null=True)
    herb_specialization = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Certification Request by {self.farmer.user.full_name}"

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductVideo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='product_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_herbal = models.BooleanField(default=False)
    active_compounds = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        qr_content = {
            "product": self.product_name,
            "farmer": self.farmer.user.full_name,
            "location": f"{self.farmer.city}, {self.farmer.state}",
            "certified": self.farmer.certification_request_set.filter(status='approved').exists(),
            "herbal_uses": self.active_compounds if self.is_herbal else None
        }
        
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(json.dumps(qr_content))
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="darkgreen", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        
        self.qr_code.save(f'qr_{self.product_id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.order_id} - {self.product.product_name}"

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('UPI', 'UPI'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Wallet', 'Wallet'),
        ('COD', 'COD'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Payment for Order {self.order.order_id}"

class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.full_name} - {self.rating} Stars"

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class ContactForm(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Resolved', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class VirtualHerbalPlant(models.Model):
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    scientific_name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)],
        help_text="The botanical name of the plant (e.g., Ocimum tenuiflorum)",
        unique=True
    )
    
    common_names = models.JSONField(
        default=list,
        help_text="List of common names for the plant (e.g., ['Tulsi', 'Holy Basil'])"
    )
    
    
    medicinal_uses = models.TextField(
        help_text="AYUSH-approved medicinal uses of the plant"
    )
    
    cultivation_guide = models.TextField(
        help_text="Detailed cultivation instructions"
    )
    
    ayush_certified = models.BooleanField(
        default=False,
        help_text="Whether the plant is AYUSH certified"
    )
    
    difficulty_level = models.CharField(
        max_length=6,
        choices=DIFFICULTY_LEVELS,
        default='medium',
        help_text="Cultivation difficulty level"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Virtual Herbal Plant"
        verbose_name_plural = "Virtual Herbal Plants"
        ordering = ['scientific_name']
        indexes = [
            models.Index(fields=['scientific_name']),
            models.Index(fields=['ayush_certified']),
        ]
    
    def __str__(self):
        return f"{self.scientific_name} ({', '.join(self.common_names[:2])})"

    def get_difficulty_color(self):
        """Helper method for UI representation"""
        return {
            'easy': 'success',
            'medium': 'warning',
            'hard': 'danger'
        }.get(self.difficulty_level, 'secondary')