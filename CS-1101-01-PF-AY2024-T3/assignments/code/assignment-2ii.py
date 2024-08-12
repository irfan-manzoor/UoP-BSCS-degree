# Define item prices
item1_price = 200.0
item2_price = 400.0
item3_price = 600.0

# Calculate total price based on selected items
def calculate_total_price(selected_items):
    total_price = 0.0

    for item in selected_items:
        if item == "Item 1":
            total_price += item1_price
        elif item == "Item 2":
            total_price += item2_price
        elif item == "Item 3":
            total_price += item3_price
        else:
            print(f"Warning: '{item}' is not a valid item.")

    return total_price

# Apply discounts based on the number of items
def apply_discount(total_price, num_items):
    if num_items == 2:
        total_price *= 0.9  # 10% discount for combo packs
    elif num_items == 3:
        total_price *= 0.75  # 25% discount for the gift pack

    return total_price

# Generate and display the catalog
def generate_catalog():
    print("Online Store")
    print("-" * 42)
    print("{:<35s}{:<10s}".format("Product(s)", "Price"))
    print("-" * 42)

    print("{:<35s}{:<10.1f}".format("Item 1", item1_price))
    print("{:<35s}{:<10.1f}".format("Item 2", item2_price))
    print("{:<35s}{:<10.1f}".format("Item 3", item3_price))

    combos = [["Item 1", "Item 2"], ["Item 2", "Item 3"], ["Item 1", "Item 3"], ["Item 1", "Item 2", "Item 3"]]
    
    for i, combo in enumerate(combos):
        combo_price = calculate_total_price(combo)
        combo_price = apply_discount(combo_price, len(combo))
        combo_name = ", ".join(combo)
        print("{:<35s}{:<10.1f}".format(f"Combo {i + 1} ({combo_name})", combo_price))

    print("-" * 42)
    print("For delivery, Contact: 98764678899")

# Call the function to generate the catalog
generate_catalog()