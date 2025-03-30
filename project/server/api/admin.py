from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    User, FarmerProfile, CustomerProfile, CertificationRequest, Category,
    Product, ProductImage, ProductVideo, Order, OrderItem, Payment, Review,
    FAQ, ContactForm, Blog, VirtualHerbalPlant
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "phone_number", "role", "is_active", "is_staff")
    search_fields = ("email", "full_name", "phone_number")
    list_filter = ("role", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("full_name", "phone_number", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "full_name", "phone_number", "role", "is_active", "is_staff"),
        }),
    )

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "expertise")
    search_fields = ("user__full_name", "city", "state")

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "created_at")
    search_fields = ("user__full_name", "phone_number")

@admin.register(CertificationRequest)
class CertificationRequestAdmin(admin.ModelAdmin):
    list_display = ("farmer", "status", "submitted_at", "approval_date")
    search_fields = ("farmer__user__full_name",)
    list_filter = ("status", "submitted_at")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description")
    search_fields = ("category_name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "farmer", "category", "price", "stock", "is_herbal")
    search_fields = ("product_name", "farmer__user__full_name")
    list_filter = ("is_herbal", "category")

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "is_featured", "created_at")

@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ("product", "video", "created_at")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer", "total_price", "order_status", "payment_status", "placed_at")
    search_fields = ("customer__email",)
    list_filter = ("order_status", "payment_status")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "payment_method", "transaction_id", "payment_status")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "rating")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status")
    list_filter = ("status",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    search_fields = ("title", "author__email")

@admin.register(VirtualHerbalPlant)
class VirtualHerbalPlantAdmin(admin.ModelAdmin):
    list_display = ("scientific_name", "ayush_certified", "difficulty_level", "created_at")
    search_fields = ("scientific_name", "common_names")
    list_filter = ("ayush_certified", "difficulty_level")
