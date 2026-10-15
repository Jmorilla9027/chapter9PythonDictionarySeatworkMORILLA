records = {}
def display_menu():
    print("\n========================")
    print("  Record Keeping App")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

def main():
    while True:
        display_menu()

        choice = input("Select an option (a, b or c): ")

        if choice == "a":
            key = input('Enter Key: ')
            value = input('Enter Value: ')

            print('Here are the Records', records)


        elif choice == "b":
            delete = input('Enter Key (For deletion): ')

        elif choice == "c":
            print("THANK YOU")

        else:
            print("Invalid choice! Please select a, b, or c.")

if __name__ == "__main__":
    main()