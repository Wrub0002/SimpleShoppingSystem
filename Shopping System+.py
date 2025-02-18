# Simple Shopping System

# Ask the user for their name
name = input("What is your name?: ")
# Ask the user for their age
age = int(input("How old are you?: "))

# Check if the user is allowed to shop
if age < 0 or age >= 100:
    print("You don't meet our requirements to shop")
    exit()

# Ask how many products the user wants to buy
num_products = int(input("How many products would you like to buy?: "))

# Initialize variables
count = 0
cart = []
total_price = 0

# Collect product details
while count < num_products:
    item = input("Enter item name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Calculate subtotal for the item
    subtotal = price * quantity
    total_price += subtotal

    # Store item details
    cart.append(f"{quantity} x {item} - ${subtotal:.2f}")

    # Increment count
    count += 1

# Ask for credit card once (after all items)
credit_card = input("Enter your credit card number: ")
final_digits = credit_card[-4:]

# Print final receipt
print("\nReceipt:")
print("---------------------------------")
print(f"Customer Name: {name}")
for product in cart:
    print(product)
print(f"Total: ${total_price:.2f}")
print(f"Payment Method: XXXX-XXXX-XXXX-{final_digits}")
print("---------------------------------")