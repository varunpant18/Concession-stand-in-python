menu = {
    "pizza": 400,
    "popcorn": 200,
    "drink": 100,
    "burger": 150,
    "fries": 100,
    "chips": 50,
    "nachos": 60}

cart = []
total = 0

print("-------Menu-------")
for key, value in menu.items():
    print(f"{key:10} : ₹{value}")
print("------------------")

while True:
    food = input("Select a food item (Q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("----Your Total----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ₹{total}")