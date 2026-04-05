from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# ==========================================================
# PRODUCT MODEL
# ==========================================================
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("pesticide", "Pesticide"),
        ("fertilizer", "Fertilizer"),
        ("seeds", "Seeds"),
        ("organic", "Organic Product"),
        ("tools", "Tools & Equipment"),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="tools")

    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # ✅ Main image
    image_main = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        default="products/default.png"
    )

    # ✅ Animated image (GIF)
    image_animated = models.ImageField(
        upload_to="products/animated/",
        blank=True,
        null=True
    )

    is_available = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.in_stock = self.stock_quantity > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ==========================================================
# CART
# ==========================================================
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


# ==========================================================
# ORDER
# ==========================================================
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cod')

    shipping_name = models.CharField(max_length=200)
    shipping_phone = models.CharField(max_length=20)
    shipping_address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.product_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"


# ==========================================================
# CROP
# ==========================================================
class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    emoji = models.CharField(max_length=10, default="🌱")

    ideal_temp_min = models.FloatField(null=True, blank=True)
    ideal_temp_max = models.FloatField(null=True, blank=True)
    ideal_soil_ph = models.FloatField(null=True, blank=True)

    market_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    growth_duration_days = models.PositiveIntegerField(default=120)
    watering_interval_days = models.PositiveIntegerField(default=7)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.emoji} {self.name}"


# ==========================================================
# CROP CALENDAR
# ==========================================================
class CropCalendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="crop_calendars")
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    field_name = models.CharField(max_length=200, default="Default Field")
    sowing_date = models.DateField(null=True, blank=True)

    week_number = models.IntegerField(default=0)
    expected_height = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop.name} ({self.field_name})"


# ==========================================================
# CROP EVENTS
# ==========================================================
class CropEvent(models.Model):
    EVENT_TYPES = [
        ('sowing', 'Sowing'),
        ('watering', 'Watering'),
        ('fertilizer', 'Fertilizer'),
        ('pesticide', 'Pesticide'),
        ('harvest', 'Harvest'),
    ]

    crop_calendar = models.ForeignKey(CropCalendar, on_delete=models.CASCADE, related_name='events')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crop_events')

    crop_name = models.CharField(max_length=100)
    field_name = models.CharField(max_length=200)

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_date = models.DateField()

    recommendation = models.CharField(max_length=255, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.crop_name} - {self.event_type}"


# ==========================================================
# DISEASE DETECTION
# ==========================================================
class DiseaseDetection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    user_image = models.ImageField(upload_to='crop_scans/')
    detected_disease = models.CharField(max_length=255, blank=True)

    confidence_score = models.FloatField(null=True, blank=True)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detected_disease or "Unknown"


# ==========================================================
# COMMUNITY
# ==========================================================
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    title = models.CharField(max_length=200)
    content = models.TextField()

    image = models.ImageField(upload_to="community/", blank=True, null=True)

    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment"


# ==========================================================
# SOIL DATA
# ==========================================================
class SoilData(models.Model):
    moisture = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Moisture: {self.moisture}"


# ==========================================================
# CROP PERFORMANCE
# ==========================================================
class CropPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    crop_name = models.CharField(max_length=100)
    yield_amount = models.FloatField()

    investment = models.FloatField()
    profit = models.FloatField()

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.crop_name


class UserCropPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    week_number = models.IntegerField()
    actual_height = models.FloatField()

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.crop.name}"