import os
import django
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartfarmingportal.settings')
django.setup()

from portal.models import Crop

print(f"Total crops in database: {Crop.objects.count()}")
print("\nAll crops:")
for crop in Crop.objects.all():
    print(f"  - {crop.id}: {crop.name}")

if Crop.objects.count() == 0:
    print("\n⚠️ No crops found! Adding default crops...")
    
    crops_data = [
        {"name": "Wheat", "emoji": "🌾", "growth_duration_days": 120, "first_fertilizer_days": 30, "second_fertilizer_days": 60, "third_fertilizer_days": 90, "first_pesticide_days": 15, "second_pesticide_days": 45, "third_pesticide_days": 75, "watering_interval_days": 7},
        {"name": "Rice", "emoji": "🍚", "growth_duration_days": 140, "first_fertilizer_days": 35, "second_fertilizer_days": 70, "third_fertilizer_days": 105, "first_pesticide_days": 20, "second_pesticide_days": 50, "third_pesticide_days": 80, "watering_interval_days": 5},
        {"name": "Cotton", "emoji": "🧵", "growth_duration_days": 180, "first_fertilizer_days": 45, "second_fertilizer_days": 90, "third_fertilizer_days": 135, "first_pesticide_days": 25, "second_pesticide_days": 75, "third_pesticide_days": 125, "watering_interval_days": 7},
        {"name": "Sugarcane", "emoji": "🎋", "growth_duration_days": 365, "first_fertilizer_days": 60, "second_fertilizer_days": 120, "third_fertilizer_days": 180, "first_pesticide_days": 30, "second_pesticide_days": 90, "third_pesticide_days": 150, "watering_interval_days": 7},
        {"name": "Soybean", "emoji": "🫘", "growth_duration_days": 90, "first_fertilizer_days": 25, "second_fertilizer_days": 50, "third_fertilizer_days": 75, "first_pesticide_days": 15, "second_pesticide_days": 40, "third_pesticide_days": 65, "watering_interval_days": 7},
        {"name": "Corn", "emoji": "🌽", "growth_duration_days": 100, "first_fertilizer_days": 30, "second_fertilizer_days": 60, "third_fertilizer_days": 80, "first_pesticide_days": 20, "second_pesticide_days": 50, "third_pesticide_days": 70, "watering_interval_days": 7},
        {"name": "Tomato", "emoji": "🍅", "growth_duration_days": 90, "first_fertilizer_days": 20, "second_fertilizer_days": 40, "third_fertilizer_days": 60, "first_pesticide_days": 10, "second_pesticide_days": 30, "third_pesticide_days": 50, "watering_interval_days": 3},
        {"name": "Potato", "emoji": "🥔", "growth_duration_days": 100, "first_fertilizer_days": 25, "second_fertilizer_days": 50, "third_fertilizer_days": 75, "first_pesticide_days": 15, "second_pesticide_days": 40, "third_pesticide_days": 65, "watering_interval_days": 7},
        {"name": "Onion", "emoji": "🧅", "growth_duration_days": 120, "first_fertilizer_days": 30, "second_fertilizer_days": 60, "third_fertilizer_days": 90, "first_pesticide_days": 15, "second_pesticide_days": 45, "third_pesticide_days": 75, "watering_interval_days": 5},
        {"name": "Chilli", "emoji": "🌶️", "growth_duration_days": 90, "first_fertilizer_days": 25, "second_fertilizer_days": 50, "third_fertilizer_days": 70, "first_pesticide_days": 15, "second_pesticide_days": 40, "third_pesticide_days": 60, "watering_interval_days": 5},
    ]
    
    for crop_data in crops_data:
        Crop.objects.get_or_create(name=crop_data["name"], defaults=crop_data)
    
    print(f"\n✅ Successfully added {Crop.objects.count()} crops!")
else:
    print("\n✅ Crops are available!")

    