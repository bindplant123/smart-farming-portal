import os
import django

# Setup Django atmosphere
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartfarmingportal.settings')
django.setup()

from portal.models import Crop, CropCalendar, Product
from django.contrib.auth.models import User

# ==========================================================
# 🌿 1. SEED CROPS (90+ Types)
# ==========================================================
crop_names = [
    'Rice','Wheat','Maize','Barley','Oats','Rye','Millet','Sorghum','Buckwheat','Quinoa',
    'Tomato','Potato','Onion','Garlic','Carrot','Cabbage','Cauliflower','Broccoli','Spinach','Lettuce',
    'Cucumber','Pumpkin','Bottle Gourd','Snake Gourd','Bitter Gourd','Capsicum','Chilli','Ginger','Turmeric','Peas',
    'Beans','Lentils','Chickpeas','Soybean','Groundnut','Mustard','Sunflower','Sesame','Cotton','Jute',
    'Sugarcane','Tobacco','Tea','Coffee','Rubber','Coconut','Oil Palm','Banana','Mango',
    'Apple','Orange','Lemon','Grape','Pomegranate','Guava','Papaya','Watermelon','Muskmelon','Strawberry',
    'Jowar','Bajra','Ragi','Kodon','Kutki','Little Millet','Proso Millet','Foxtail Millet','Barnyard Millet','Amaranth',
    'Methi','Coriander','Mint','Basil','Ajwain','Cumin','Fennel','Fenugreek','Black Pepper',
    'Cardamom','Cinnamon','Cloves','Nutmeg','Mace','Vanilla','Tamarind','Kokum','Jackfruit','Ber',
    'Aonla','Fig','Date Palm','Almond','Walnut','Pistachio','Cashew','Pineapple','Kiwi','Dragon Fruit'
]

print("🌱 Seeding Crops...")
for name in crop_names:
    crop, created = Crop.objects.get_or_create(
        name=name,
        defaults={
            "growth_duration_days": 90,
            "market_price": 50.00
        }
    )
    if created:
        for week in range(1, 21):
            CropCalendar.objects.get_or_create(
                crop=crop,
                week_number=week,
                defaults={"expected_height": week * 5}
            )

# ==========================================================
# 🛒 2. SEED PRODUCTS (Market Data)
# ==========================================================
products_data = [
    {'name': 'Urea Fertilizer', 'category': 'fertilizer', 'price': 450.0, 'brand': 'IFFCO', 'stock_quantity': 100},
    {'name': 'NPK 19:19:19', 'category': 'fertilizer', 'price': 600.0, 'brand': 'Mahadhan', 'stock_quantity': 50},
    {'name': 'Neem Oil Pesticide', 'category': 'pesticide', 'price': 300.0, 'brand': 'Organic India', 'stock_quantity': 40},
    {'name': 'Monocrotophos', 'category': 'pesticide', 'price': 800.0, 'brand': 'Bayer', 'stock_quantity': 20},
    {'name': 'Hybrid Rice Seeds', 'category': 'seeds', 'price': 1200.0, 'brand': 'Pioneer', 'stock_quantity': 30},
    {'name': 'Wheat Seeds HD-2967', 'category': 'seeds', 'price': 1500.0, 'brand': 'National Seeds', 'stock_quantity': 25},
    {'name': 'Hand Sprayer (5L)', 'category': 'tools', 'price': 950.0, 'brand': 'ASPEE', 'stock_quantity': 15},
    {'name': 'Drip Irrigation Kit', 'category': 'tools', 'price': 5000.0, 'brand': 'Jain Irrigation', 'stock_quantity': 5},
    {'name': 'Soil pH Meter', 'category': 'tools', 'price': 1200.0, 'brand': 'Generic', 'stock_quantity': 10},
    {'name': 'Cow Dung Manure', 'category': 'organic', 'price': 200.0, 'brand': 'Local', 'stock_quantity': 200},
    {'name': 'Vermicompost', 'category': 'organic', 'price': 400.0, 'brand': 'EcoFarm', 'stock_quantity': 150},
]

print("🛒 Seeding Products...")
for item in products_data:
    Product.objects.get_or_create(
        name=item['name'],
        defaults={
            'category': item['category'],
            'price': item['price'],
            'brand': item['brand'],
            'stock_quantity': item['stock_quantity'],
            'description': f"High quality {item['name']} for better yield."
        }
    )

# ==========================================================
# 🔐 3. CREATE SUPERUSER (Optional)
# ==========================================================
if not User.objects.filter(username="admin").exists():
    print("👤 Creating Superuser...")
    User.objects.create_superuser("admin", "admin@example.com", "admin123")

print("✅ Seeding Complete!")
