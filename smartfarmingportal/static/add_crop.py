import os
import django
import sys

# Setup Django settings
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartfarmingportal.settings')
django.setup()

from portal.models import Crop

# List of crops to add
crops_list = [
    "Wheat", "Rice", "Cotton", "Sugarcane", "Soybean",
    "Corn", "Barley", "Pulses", "Groundnut", "Sunflower",
    "Mustard", "Jowar", "Bajra", "Maize", "Turmeric",
    "Ginger", "Onion", "Tomato", "Potato", "Chilli",
    "Garlic", "Cumin", "Coriander", "Paddy", "Urad",
    "Moong", "Arhar", "Gram", "Peas", "Coffee"
]

# Add crops to database
for name in crops_list:
    Crop.objects.get_or_create(name=name)

print(f"✅ Successfully added {Crop.objects.count()} crops!")