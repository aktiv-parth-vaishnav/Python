dic = {}

def create():
    countries = input("Enter countries (comma-separated): ").strip().split(",")
    for country in countries:
        print(country)

        if country:
            dic[country] = {}

    print("countries added:", list(dic.keys()))

    while True:
        print("Enter states (type '0' to finish):")
        parent_country = input("Enter a country name to add state for: ").strip()
        if parent_country == "0":
            break
        if parent_country in dic:
            state = input(f"Enter state(s) for {parent_country} (comma-separated): ").strip().split(",")
            for s in state:
                s = s.strip()
                if s:
                    dic[parent_country][s] = []
        else:
            print("Country not found.")

    while True:
        print("\nEnter cities (type '0' to finish):")
        parent_country = input("Enter a country name: ").strip()
        if parent_country == "0":
            break
        if parent_country in dic:
            parent_state = input("Enter a state name to add city for: ").strip()
            if parent_state in dic[parent_country]:
                cities = input(f"Enter city(s) for {parent_state} (comma-separated): ").strip().split(",")
                for c in cities:
                    c = c.strip()
                    if c:
                        dic[parent_country][parent_state].append(c)
            else:
                print("State not found.")
        else:
            print("Country not found.")

    print("Data Created Successfully.")
    print(dic)


def update():
    print("Update Menu:")
    print("1. Add new country")
    print("2. Add state to country")
    print("3. Add city to state")
    choice = input("Choose option: ")

    if choice == "1":
        countries = input("Enter new country(s) (comma-separated): ").strip().split(",")
        for country in countries:
            country = country.strip()
            if country and country not in dic:
                dic[country] = {}
    elif choice == "2":
        country = input("Enter country name: ").strip()
        if country in dic:
            states = input(f"Enter state(s) for {country} (comma-separated): ").strip().split(",")
            for s in states:
                s = s.strip()
                if s and s not in dic[country]:
                    dic[country][s] = []
        else:
            print("Country not found.")
    elif choice == "3":
        country = input("Enter country name: ").strip()
        if country in dic:
            state = input("Enter state name: ").strip()
            if state in dic[country]:
                cities = input(f"Enter city(s) for {state} (comma-separated): ").strip().split(",")
                for c in cities:
                    c = c.strip()
                    if c and c not in dic[country][state]:
                        dic[country][state].append(c)
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
        country = input("Enter country name: ").strip()
        if country in dic:
            del dic[country]
        else:
            print("Country not found.")
    elif choice == "2":
        country = input("Enter country name: ").strip()
        if country in dic:
            state = input("Enter state name: ").strip()
            if state in dic[country]:
                del dic[country][state]
            else:
                print("State not found.")
        else:
            print("Country not found.")
    elif choice == "3":
        country = input("Enter country name: ").strip()
        if country in dic:
            state = input("Enter state name: ").strip()
            if state in dic[country]:
                city = input("Enter city name: ").strip()
                if city in dic[country][state]:
                    dic[country][state].remove(city)
                else:
                    print("City not found.")
            else:
                print("State not found.")
        else:
            print("Country not found.")


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
        print(dic)
    elif action == "5":
        break
    else:
        print("Invalid option.")
