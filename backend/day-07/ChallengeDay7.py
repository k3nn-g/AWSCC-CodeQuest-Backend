def menu():
    print("\nOptions: ")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

shoppinglist = []

def additem(shoppinglist):
    item = input("Enter the item to add: ").capitalize()
    shoppinglist.append(item)
    print(f"{item} has been added to your shopping list.")

def removeitem(shoppinglist):
    item = input("Enter the item you want to remove: ").capitalize()
    if item in shoppinglist:
        shoppinglist.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"The item you entered is not in your Shopping List.")

def viewlist(shoppinglist):
    if not shoppinglist:
        print(f"The shopping list is empty.")
    else: 
        print(f"\nYour Shopping list: ")
        for list, item in enumerate(shoppinglist, start=1):
            print(f"{list}. {item}")

def main ():
    while True:
        menu()
        choice = input("Enter the number of your choice (1-4): ")
        
        if choice == '1':
            additem(shoppinglist)
        elif choice == '2':
            viewlist(shoppinglist)
        elif choice == '3':
            removeitem(shoppinglist)
        else:
            print(f"Goodbye!")
            break

if __name__ == "__main__" :
    main()
