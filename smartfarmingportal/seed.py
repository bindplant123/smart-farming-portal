from portal.models import Crop, CropCalendar

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

print("Adding crops...")

for i, name in enumerate(crop_names, 1):

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

    if i % 10 == 0:
        print(f"Added {i} crops...")

print("Done!")