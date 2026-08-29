import os
os.system('cls')
subscriptions=[]
while True:
    total_subscriptions = (input("Enter the number of subscriptions you have: "))
    if not total_subscriptions.isdigit():
        print("Please enter a valid amount of subscriptions!!")
    else:
        total_subscriptions = int(total_subscriptions)
        if total_subscriptions <= 0:
            print("Please enter a valid amount of subscriptions!!")
        else:
            break
print()

for x in range(total_subscriptions):
    while True:
        subscription_name = input(f"Enter the name of subscription #{x + 1}: ")
        if subscription_name == "":
            print("Please enter a valid subscription name!!")
        else:
            duplicate = False
            for subscription in subscriptions:
                if subscription['Name'].lower() == subscription_name.lower():
                    duplicate = True
                    break
            if duplicate:
                print(f"You already entered this subscription, please enter a different one!")
            else:
                break

    print("""Please choose one of the following categories for your subscription: 
    1. Entertainment
    2. Shopping and Groceries
    3. Music
    4. Others(Enter your category)""")
    print()

    while True:
        subscription_category = input("Enter the category that best suits your subscription (1,2,3 or 4): ")

        if not subscription_category.isdigit():
            print("Please enter a valid category!!")
            continue

        subscription_category = int(subscription_category)

        if subscription_category < 1 or subscription_category > 4:
            print("Please enter a number between 1 and 4!!")
            continue

        break

    match subscription_category:
        case 1:
            subscription_category = "Entertainment"
            break
        case 2:
            subscription_category = "Shopping and Groceries"
            break
        case 3:
            subscription_category = "Music"
            break
        
        case 4:
            while True:
                subscription_category = input("Enter your category: ").strip()

                if subscription_category == "":
                    print("Please enter a valid category!!")
                else:
                    break

    while True:
        subscription_cost = input(f"Enter the monthly cost of the subscription #{x + 1} (in ₹): ")

        if not subscription_cost.isdigit():
            print("Please enter a valid subscription cost!!")
        else:
            subscription_cost = int(subscription_cost)
            if subscription_cost <= 0:
                print("Please enter a valid subscription cost!!")
            else:
                break

    print()
    subscription = {'Name': subscription_name, 'Category': subscription_category, 'Cost': subscription_cost}
    subscriptions.append(subscription)
print()
def display_summary():
    total = 0
    for subscription in subscriptions:
        total += subscription['Cost']

        if len(subscriptions) == 0:
            print("You currently have no subscriptions.")
            return

        print(f"Your total spending per month on subscriptions is ₹{total}")

    for subscription in subscriptions:
        print(f"{subscription['Name']} : ₹{subscription['Cost']}/month")

    print()
    print(f"Your total spending per year on subscriptions is ₹{total * 12}")
    print()
    
    categories = []

    for subscription in subscriptions:
        category = subscription['Category']

        if category not in categories:
            categories.append(category)

    for category in categories:

        count = 0

        print(f"{category}:")

        for subscription in subscriptions:

            if subscription['Category'] == category:
                print(f"{subscription['Name']} : ₹{subscription['Cost']}")
                count += 1

        print()

        if count > 1:

            print(f"You have {count} {category} subscriptions:")

            for subscription in subscriptions:

                if subscription['Category'] == category:
                    print(subscription['Name'])

            print(f"Consider reviewing whether you need all {count} subscriptions.")

            print()

display_summary()

subscription_remove = input("Would you like to remove any subscription (leave empty to quit): ")
while True:
    if subscription_remove == "":
        break

    found = False

    for subscription in subscriptions:
            
            if subscription['Name'].lower() == subscription_remove.lower():
                subscriptions.remove(subscription)
                print(f"{subscription['Name']} has been removed!")
                found = True
                break
    
    if not found:
        print("Subscription not found!")

    subscription_remove = input("Would you like to remove any other subscription (leave empty to quit): ")

print()
print("Updated subscription information:")
print()

display_summary()