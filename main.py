from js import document

restaurant_name = "Clash Cookies"
# string data type → restaurant name

owner_name = "John Vincent T. Ligas"
# string data type → owner's name

year_established = 2025
# integer data type → year established

popular_item_price = 200.00
# float data type (updated to match Pekka Pancakes price as popular item)

has_delivery = True
# boolean data type → business has delivery

# ✅ Updated product list to match order page
product_names = [
    "Mini Cookie", 
    "Butterfly Surprise", 
    "Goblin Delight", 
    "Barbarian Rage Juice", 
    "Pekka Pancakes"
]

business_hours = {
    "Monday": "9 AM - 9 PM",
    "Tuesday": "9 AM - 9 PM",
    "Wednesday": "9 AM - 9 PM",
    "Thursday": "9 AM - 9 PM",
    "Friday": "9 AM - 10 PM",
    "Saturday": "10 AM - 10 PM",
    "Sunday": "10 AM - 8 PM"
}
# dictionary data type → operating hours

# ✅ Updated prices to match the order page
menu_prices = {
    "Mini Cookie": 75.00,
    "Butterfly Surprise": 140.00,
    "Goblin Delight": 180.00,
    "Barbarian Rage Juice": 60.00,
    "Pekka Pancakes": 200.00
}

# ✅ Expanded allergens list for new items
common_allergens = {
    "Mini Cookie": ["gluten", "dairy"],
    "Butterfly Surprise": ["nuts", "eggs"],
    "Goblin Delight": ["soy", "peanuts"],
    "Barbarian Rage Juice": ["artificial color", "sugar"],
    "Pekka Pancakes": ["gluten", "eggs", "dairy"]
}

tax_rate = 0.12
# float data type → VAT/tax rate

# Owner info section
owner_info = (
    "<h2>About Us</h2>"
    "<p><b>Owner:</b> " + owner_name + "</p>"
    "<p><b>Established:</b> " + str(year_established) + "</p>"
    "<p><b>Popular Item Price:</b> ₱" + str(popular_item_price) + "</p>"
    "<p><b>Delivery:</b> " + ("Yes" if has_delivery else "No") + "</p>"
    "<p><b>Tax Rate:</b> " + str(tax_rate * 100) + "%</p>"
)
document.getElementById("owner-info").innerHTML = owner_info

# Business hours section
hours_html = "<h2>Business Hours</h2><ul>"
for day, hours in business_hours.items():
    hours_html += "<li><b>" + day + ":</b> " + hours + "</li>"
hours_html += "</ul>"
document.getElementById("business-hours").innerHTML = hours_html

# ✅ Menu section now includes new items with updated prices
menu_html = "<h2>Menu</h2><ul>"
for item in product_names:
    price = menu_prices.get(item, "N/A")
    menu_html += "<li><b>" + item + ":</b> ₱" + str(price) + "</li>"
menu_html += "</ul>"
document.getElementById("menu").innerHTML = menu_html

# ✅ Allergens updated for new products
allergen_html = "<h2>Common Allergens</h2><ul>"
for item, allergens in common_allergens.items():
    allergen_html += "<li><b>" + item + ":</b> " + ", ".join(allergens) + "</li>"
allergen_html += "</ul>"
document.getElementById("allergens").innerHTML = allergen_html
