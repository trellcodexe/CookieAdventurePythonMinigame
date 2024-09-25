import random

print("Welcome to 'Martha's Cookie Adventure!'")

# Start the game loop
playing = True

while playing:
    # Step 1: Choose a store
    store = input("\nChoose a store for Martha to go to (e.g., SuperMart, CookieTown, BakeShop): ")

    # Step 2: Choose the type of cookies
    cookie_type = input("What kind of cookies should Martha buy? (e.g., Chocolate Chip, Oatmeal, Peanut Butter): ")

    # Step 3: Set Martha's budget
    try:
        budget = float(input("Enter Martha's budget in dollars: "))
    except ValueError:
        print("Invalid input. Setting budget to $10.")
        budget = 10

    # Check if cookies are available at the store
    print(f"\nMartha goes to {store} to buy {cookie_type} cookies.")

    # Randomly determine if the cookies are available and the price
    cookies_available = random.choice([True, False])
    cookie_price = round(random.uniform(5, 15), 2)  # Price between $5 and $15

    # Step 4: Branching logic to decide what happens next
    if cookies_available:
        print(f"The {cookie_type} cookies are available and cost ${cookie_price:.2f}.")
        if cookie_price <= budget:
            print("Martha buys the cookies! 🎉")
            # Ask if the player wants to play again
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                playing = False
        else:
            print("Martha doesn't have enough money to buy the cookies. 😢")
            # Branching: Offer to increase budget
            more_money = input("Do you want to add more money to the budget? (yes/no): ").strip().lower()
            if more_money == "yes":
                additional_funds = float(input("How much more do you want to add?: "))
                budget += additional_funds
                print(f"Martha's new budget is ${budget:.2f}. Let's try again!")
            else:
                print("Martha goes home without cookies.")
                playing = False
    else:
        print(f"Unfortunately, the {cookie_type} cookies are out of stock. 😢")
        # Branching: Offer to try a different store
        try_again = input("Do you want to try a different store? (yes/no): ").strip().lower()
        if try_again != "yes":
            playing = False

print("Game Over! Thanks for playing!")
