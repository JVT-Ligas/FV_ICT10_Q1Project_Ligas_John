from pyscript import document, display


# Updated product list to match order page
product_names = [
    "Mini Cookie", 
    "Butterfly Surprise", 
    "Goblin Delight", 
    "Barbarian Rage Juice", 
    "Pekka Pancakes"
]

# Updated prices to match the order page
menu_prices = {
    "Mini Cookie": 75.00,
    "Butterfly Surprise": 140.00,
    "Goblin Delight": 180.00,
    "Barbarian Rage Juice": 60.00,
    "Pekka Pancakes": 200.00,
}

# Event handler for order button
def on_click(event):
    order = [
        menu 
        for menu in product_names 
        if document.getElementById(f"menu{menu.replace(' ', '')}").checked
    ]

    name = document.getElementById("name").value.strip()
    address = document.getElementById("address").value.strip()
    phone = document.getElementById("phone").value.strip()

    # Input validation
    if not name or not address or not phone:
        display("⚠️ Please fill out all fields before placing an order.", target="string")
        return
    if not phone.isdigit() or len(phone) < 7 or len(phone) > 11:
        display("⚠️ Please enter a valid phone number (7–11 digits).", target="string")
        return
    if not order:
        display("⚠️ Please select at least one product to order.", target="string")
        return
    
    # Clear previous message
    document.getElementById("string").textContent = ""

    # Calculate total price
    total_price = sum(menu_prices[item] for item in order)
    formatted_price = f"₱{total_price:,.2f}"

    # Create order summary
    info = (
        f"Order Info and Summary\n"
        f"-----------------------\n"
        f"Name:\t{name}\n"
        f"Address:\t{address}\n"
        f"Phone Number:\t{phone}\n\n"
        f"Summary:\n"
        f"----------------------\n"
        f"Order for: {name},\n"
        f"Please deliver at {address}, contact number {phone}.\n"
        f"Customer order: {', '.join(order)}\n"
        f"Price to be paid: {formatted_price}"
    )

    # Show summary
    display(info, target="string")

