dic = {}

def action_create():
    # Add Countries
    available = []
    countries = input("Enter countries (comma-separated): ").strip().split(",")
    for country in countries:
        key = country.strip().lower()
        if key not in dic:
            dic[key] = {}
        else:
            available.append(country)
    if available:
        print(f"Already exists: {','.join(available)}")
    print("Available:", dic)

    # Add States
    while True:
        print("\nEnter states (type '0' to finish):")
        parent_country = input("Enter a country name to add state for: ").strip().lower()
        if parent_country == "0":
            break
        if parent_country in dic:
            states = input(f"Enter state(s) for {parent_country} (comma-separated): ").strip().split(",")
            available_state = []
            for s in states:
                key = s.strip().lower()
                if key not in dic[parent_country]:
                    dic[parent_country][key] = []
                else:
                    available_state.append(s)
            if available_state:
                print(f"Already exists: {','.join(available_state)}")
            print("Available:", dic)
        else:
            print("Country not found.")

    # Add Cities
    while True:
        print("\nEnter cities (type '0' to finish):")
        parent_country = input("Enter a country name: ").strip().lower()
        if parent_country == "0":
            break
        if parent_country in dic:
            parent_state = input("Enter a state name to add city for: ").strip().lower()
            available_cities = []
            if parent_state in dic[parent_country]:
                cities = input(f"Enter city(s) for {parent_state} (comma-separated): ").strip().split(",")
                for c in cities:
                    key = c.strip().lower()
                    if key not in dic[parent_country][parent_state]:
                        dic[parent_country][parent_state].append(key)
                    else:
                        available_cities.append(c)

                if available_cities:
                    print(f"Already City Exists: {','.join(available_cities)}")
                print("Available:", dic)
            else:
                print("State not found.")
        else:
            print("Country not found.")

    print("Data Created Successfully.")
    print(dic)


def action_update():
    if not dic:
        print("No data available to update.")
        return
    print(dic)


    print("1. Update Country Name")
    print("2. Update State Name")
    print("3. Update City Name")
    choice = input("Enter choice (1-3): ")

    #Update country name
    if choice == "1":
        country = input("Enter current country name: ").lower()
        if country not in dic:
            print("Country not found.")
        new_country = input("Enter new country name: ")
        if new_country in dic:
            print("country already exists.")

        dic[new_country] = dic.pop(country)
        print("Country updated successfully.")

    # Update state name
    elif choice == "2":
        country = input("Enter country name: ")
        if country not in dic:
            print("Country not found.")

        state = input("Enter current state name: ")
        if state not in dic[country]:
            print("State not found.")

        new_state = input("Enter new state name: ")
        if new_state in dic[country]:
            print("That state already exists.")

        dic[country][new_state] = dic[country].pop(state)
        print("State updated successfully.")

    # Update city name
    elif choice == "3":
        country = input("Enter country name: ")
        if country not in dic:
            print("Country not found.")
        state = input("Enter state name: ")
        if state not in dic[country]:
            print("State not found.")

        city = input("Enter current city name: ")
        if city not in dic[country][state]:
            print("City not found.")
        new_city = input("Enter new city name: ")
        if new_city in dic[country][state]:
            print("That city already exists.")
        # Replace city in list
        index = dic[country][state].index(city)
        dic[country][state][index] = new_city
        print("City updated successfully.")

    else:
        print("Invalid choice.")


def action_delete():
    print("Delete Menu:")
    print("1. Delete country")
    print("2. Delete state")
    print("3. Delete city")
    choice = input("Choose option: ")
    print(dic)

    if choice == "1":
        country = input("Enter country name: ").strip().lower()
        if country in dic:
            del dic[country]
        else:
            print("Country not found.")

    elif choice == "2":
        country = input("Enter country name: ").strip().lower()
        if country in dic:
            state = input("Enter state name: ").strip().lower()
            if state in dic[country]:
                del dic[country][state]
            else:
                print("State not found.")
        else:
            print("Country not found.")

    elif choice == "3":
        country = input("Enter country name: ").strip().lower()
        if country in dic:
            state = input("Enter state name: ").strip().lower()
            if state in dic[country]:
                city = input("Enter city name: ").strip().lower()
                if city in dic[country][state]:
                    dic[country][state].remove(city)
                else:
                    print("City not found.")
            else:
                print("State not found.")
        else:
            print("Country not found.")


# Main menu
while True:
    print("\nMain Menu:")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Show Data")
    print("5. Exit")
    action = input("Choose an option: ")
    if action == "1":
        action_create()
    elif action == "2":
        action_update()
    elif action == "3":
        action_delete()
    elif action == "4":
        print(dic)
    elif action == "5":
        break
    else:
        print("Invalid option.")
