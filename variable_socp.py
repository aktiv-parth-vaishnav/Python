dic = {}
def create():
    # Add Countrie
    """
    Create a new record with unique values User can not
    enter a new
    """
    available=[]
    countries = input("Enter countries (comma-separated): ").strip().split(",")
    for country in countries:
        key = country.strip().lower()
        if key not in dic:
            dic[key] = {}
        else:
            available.append(country)

    print(f"Already exists: {','.join(available)}")
    print("available", dic)

    # Add States
    while True:
        print("\nEnter states (type '0' to finish):")
        parent_country = input("Enter a country name to add state for: ").strip().lower()
        if parent_country == "0":
            break
        if parent_country in dic:
            states = input(f"Enter state(s) for {parent_country} (comma-separated): ").strip().split(",")
            available_state=[]
            for s in states:
                key = s.strip().lower()
                if key not in dic[parent_country]:
                    dic[parent_country][key] = []
                else:
                    available_state.append(s)
            print(f"Already exists: {','.join(available_state)}")
            print("available", dic)
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
            availible_cities=[]
            if parent_state in dic[parent_country]:
                cities = input(f"Enter city(s) for {parent_state} (comma-separated): ").strip().split(",")
                for c in cities:
                    key = c.strip().lower()
                    if key not in dic[parent_country][parent_state]:
                        dic[parent_country][parent_state].append(key)
                    else:
                        availible_cities.append(c)
                        # print(f" Already available city: {c}")
                        # print(f" Already available city: {c.strip()}")
                    print(f"Already City Exists: {','.join(availible_cities)}")
                    print("available", dic)

            else:
                print("State not found.")
        else:
            print("Country not found.")

    print("\nData Created Successfully.")
    print(dic)


def update():
    print("\nUpdate Menu:")
    print("1. Add new country")
    print("2. Add state to country")
    print("3. Add city to state")
    choice = input("Choose option: ")
    if choice == "1":
        countries = input("Enter new country(s) (comma-separated): ").strip().split(",")
        for country in countries:
            key = country.strip().lower()
            if key not in dic:
                dic[key] = {}
            else:
                print(f" Already available country: {country.strip()}")
    elif choice == "2":
        country = input("Enter country name: ").strip().lower()
        if country in dic:
            states = input(f"Enter state(s) for {country} (comma-separated): ").strip().split(",")
            for s in states:
                key = s.strip().lower()
                if key not in dic[country]:
                    dic[country][key] = []
                else:
                    print(f"Already available state: {s.strip()}")
        else:
            print("Country not found.")
    elif choice == "3":
        country = input("Enter country name: ").strip().lower()
        if country in dic:
            state = input("Enter state name: ").strip().lower()
            if state in dic[country]:
                cities = input(f"Enter city(s) for {state} (comma-separated): ").strip().split(",")
                for c in cities:
                    key = c.strip().lower()
                    if key not in dic[country][state]:
                        dic[country][state].append(key)
                    else:
                        print(f"Already available city: {c.strip()}")
            else:
                print("State not found.")
        else:
            print("Country not found.")


def delete():
    print("\nDelete Menu:")
    print("1. Delete country")
    print("2. Delete state")
    print("3. Delete city")
    choice = input("Choose option: ")
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
        create()
    elif action == "2":
        update()
    elif action == "3":
        delete()
    elif action == "4":
        print(dic)
    elif action == "5":
        break
    else:
        print("Invalid option.")
