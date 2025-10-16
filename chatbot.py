import json

# Load database
with open("database.json", "r") as f:
    db = json.load(f)

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today? (Search product / Order status / Help)"

    # Search products
    if "buy" in user_input or "search" in user_input:
        product_name = user_input.replace("buy", "").replace("search", "").strip()
        for product in db["products"]:
            if product_name.lower() in product["name"].lower():
                return f"{product['name']} is available for ₹{product['price']}."
        return "Sorry, that product is not available."

    # Order status
    if "order" in user_input:
        for order in db["orders"]:
            if order["order_id"] in user_input:
                return f"Your order {order['order_id']} is {order['status']}."
        return "I couldn’t find your order. Please check the Order ID."

    # Help
    if "help" in user_input:
        return "You can ask me:\n- Search for a product\n- Check order status\n- Get help"

    return "Sorry, I didn’t understand that. Try again!"

# Chat loop
print("Chatbot: Hello! Welcome to the E-commerce Chatbot.")
while True:
    user_in = input("You: ")
    if user_in.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_in))