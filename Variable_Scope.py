
dic = {

    "country": [],
    "state": [],
    "city": []
}


def create():
    while True:
        country = input("Enter a Country (or 0 to finish): ").strip()
        if country == '0':
            break
        if country:
            dic["country"].append(country)

    print("Enter states (enter 0 to finish):")
    while True:
        state = input("Enter a State: ").strip()
        if state == '0':
            break
        dic["state"].append(state)

    print("Enter cities (enter 0 to finish):")
    while True:
        city = input("Enter a City: ").strip()
        if city == '0':
            break
        dic["city"].append(city)

    print("Data Created Successfully.")
    print(dic)


def update():
    print("What do you want to update?")
    print("Options: state, country, city")
    option = input("Enter your choice: ").lower()

    if option == "state":
        print(f"Current States: {dic['state']}")
        print("1. Add new states")
        print("2. Rename existing state")
        choice = input("Choose option 1 or 2: ")
        if choice == "1":
            while True:
                s = input("New state (type 0 to finish): ")
                if s == '0':
                    break
                dic["state"].append(s)
        elif choice == "2":
            old = input("Which state to rename?: ")
            if old in dic["state"]:
                new = input("New state name: ")
                index = dic["state"].index(old)
                dic["state"][index] = new
            else:
                print("State not found.")

    elif option == "city":
        print(f"Current Cities: {dic['city']}")
        print("1. Add new cities")
        print("2. Rename existing city")
        choice = input("Choose option 1 or 2: ")
        if choice == "1":
            while True:
                c = input("New city (type 0 to finish): ")
                if c == '0':
                    break
                dic["city"].append(c)
        elif choice == "2":
            old = input("Which city to rename?: ")
            if old in dic["city"]:
                new = input("New city name: ")
                index = dic["city"].index(old)
                dic["city"][index] = new
            else:
                print("City not found.")

    elif option == "country":
        print(f"Current Countries: {dic['country']}")
        print("1. Add new country")
        print("2. Rename existing country")
        choice = input("Choose option 1 or 2: ")
        if choice == "1":
            while True:
                c = input("New country (type 0 to finish): ")
                if c == '0':
                    break
                dic["country"].append(c)
        elif choice == "2":
            old = input("Which country to rename?: ")
            if old in dic["country"]:
                new = input("New country name: ")
                index = dic["country"].index(old)
                dic["country"][index] = new
            else:
                print("Country not found.")

    else:
        print("Invalid choice.")

    print("Updated dictionary:")
    print(dic)


def delete():
    print("What do you want to delete?")
    print("Options: state, city, country")
    choice = input("Enter your choice: ").lower()

    if choice == "state":
        print(f"Current States: {dic['state']}")
        item = input("Enter the state to delete: ")
        if item in dic["state"]:
            dic["state"].remove(item)
            print("State found.")
        else:
            print("State not found.")

    elif choice == "city":
        print(f"Current Cities: {dic['city']}")
        item = input("Enter the city to delete: ")
        if item in dic["city"]:
            dic["city"].remove(item)
            print("City found.")
        else:
            print("City not found.")

    elif choice == "country":
        item = input("Enter the country to delete: ")
        if item in dic["country"]:
            dic["country"].remove(item)
            print("Country found.")
        else:
            print("Country not found.")
    else:
        print("Invalid choice.")

    print("Updated dictionary after deletion:")
    print(dic)


while True:
    print("Main Menu:")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Show Data")
    print("5. Exit")
    action = input("Choose an option: ")

    if action == "1":
        create()
    elif action == "2":
        update()
    elif action == "3":
        delete()
    elif action == "4":
        print("Current Data:")
        print(dic)
    elif action == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid option.")