#create a list
market_list = []

#Get input from user
while True:
    print('\nWhat would you like to do with this list? \n')
    print("1. Add to the list")
    print("2. View the list")
    print("3. Check if an item is in the list")
    print("4. Delete an object from the list")
    print("5. Clear the list")
    print("6. Exit \n")

    user_input = input("Enter an option number: ")
    
    if user_input == "1":
        items = input("Enter an item to be added to the list: \n")
        market_list.append(items)
        print(f"{items} has been added to the list")
    elif user_input == "2":
        if not market_list:
            print("The market list is empty")
        else:
            for index, item in enumerate(market_list):
                print(f"{index+1}. {item}")
    elif user_input == "3":
        item = input("Enter an item to be checked")
        if item in market_list:
            print(f"{item} is in market list")
        else:
            print(f"{item} is not in market list")
    elif user_input == "4":
        for index, item in enumerate(market_list):
            print(f"{index}. {item}")
        to_delete = int(input("Enter index number to remove: "))
        removed_item = market_list.pop(to_delete)
        print(f"{removed_item} has been removed from the list")
    elif user_input == "5":
        market_list.clear()
        print("Items cleared")
    elif user_input == "6":
        print("Exiting program..... Goodbye!")
        break
    
    else:
        print("Invalid option number")