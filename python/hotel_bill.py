import random

token = random.randint(10, 99)
menu = {
    1: {"sandwich": 40},
    2: {"coffee": 20},
    3: {"juice": 30}
}

print("=== MENU ===")
for key, value in menu.items():
    for item, price in value.items():
        print(f"{key}. {item} - Rs.{price}")

while True:
    mobile = input("Mobile number: ")
    email = input("Enter email: ")
    print("Your token is:", token)

    total = 0
    while True:
        bill = input("Enter item number (or 'q' to quit): ")
        if bill == 'q':
            break

        if bill.isdigit():
            item = int(bill)
            if item in menu:
                price = list(menu[item].values())[0]
                name = list(menu[item].keys())[0]
                total += price
                # print(f"Added {name} for Rs.{price}")
            else:
                print("Invalid item number!")
        else:
            print("Please enter a valid number or 'q'.")

    print("\n--- BILL ---")
    print("Mobile no. :", mobile)
    print("Email      :", email)
    print("Total Bill :", total)
    print("Thank you for visiting!\n")
