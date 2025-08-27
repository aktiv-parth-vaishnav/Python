import csv  # use built-in csv

def action_create():
    """
     this method data is variable which is global and  country state_ans city_ans  is just take input and either or user enter a data or not
    """
    global data
    while True:
        country = input("you want add country? y/n = ")
        if country == 'n':
            if data:
                print("your Data is: ", data)
            return
        elif country != 'y':
            print("not correct choice")
            continue
        else:
            country_name = input("give country name: ")
            if country_name in data:
                print("Already added. Try remove or give new")
                continue
            data[country_name] = {}
            while True:
                state_ans = input(f"want to add state in {country_name}? y/n = ")
                if state_ans == 'n':
                    break
                elif state_ans != 'y':
                    print("not correct choice")
                    continue
                else:
                    state_name = input("state name: ")
                    if state_name in data[country_name]:
                        print(f"Already added {state_name} in {country_name}")
                        continue
                    data[country_name][state_name] = []
                    while True:
                        city_ans = input(f"Add city in {state_name}? y/n = ")
                        if city_ans == 'n':
                            break
                        elif city_ans != 'y':
                            print("not correct choice")
                            continue
                        else:
                            city_name = input("City name: ")
                            if city_name in data[country_name][state_name]:
                                print("Already exist, try other name.")
                                continue
                            data[country_name][state_name].append(city_name)


Final_data = []


def dicttolist(dictt):
    """
    take data input in form of dict and conver insert in to list to add in sheet
    """

    if not dictt:
        print("No data found.")
        return
    for Cntry in dictt:
        if dictt[Cntry] == {}:
            row = [Cntry, "", ""]
            Final_data.append(row)
            continue
        for st_idx, st in enumerate(dictt[Cntry]):
            row = [Cntry if st_idx == 0 else "", st]
            if not dictt[Cntry][st]:
                row.append("")
                Final_data.append(row)
            else:
                for ct_idx, ct in enumerate(dictt[Cntry][st]):
                    if ct_idx == 0:
                        Final_data.append(row + [ct])
                    else:
                        Final_data.append(["", "", ct])


data = {}

while True:
    chs = input("\nmake from fix data = inbuild\nmake new data = new\nWhat u want: ")
    match chs:
        case "inbuild":
            dicttolist({
                'India': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]},
                'Pakistan': {"Sindh": ['Karachi', "Hyderabad"], 'Punjab': ["Lahore", "Multan"]}
            })
            break
        case "new":
            action_create()
            dicttolist(data)
            break
        case _:
            print("Plz give correct opt")

with open("output.csv", 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(["Country", "State", "City"])
    wr.writerows(Final_data)

print("CSV file created successfully!")
