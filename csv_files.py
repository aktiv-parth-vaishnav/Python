import csv
def creet():

    global Dataa
    while True:
        Cuntry_ans = input("you want add cuntry? y/n = ")
        if Cuntry_ans == 'n':
            if not Dataa:
                pass
            else:
                print("your Data is: ")
            return
        elif Cuntry_ans != 'y':
            print("not correct choice")
            continue
        else:
            Cuntry_nm = input("give country name: ")
            if Cuntry_nm in Dataa:
                print("Already added. Try remove or give new")
                continue
            Dataa[Cuntry_nm] = {}
            while True:
                Stat_ans = input(f"want to add state in {Cuntry_nm}? y/n = ")
                if Stat_ans == 'n':
                    break
                elif Stat_ans != 'y':
                    print("not correct choice")
                    continue
                else:
                    Stat_nm = input("state name: ")
                    if Stat_nm in Dataa[Cuntry_nm]:
                        print(f"Already added {Stat_nm} in {Cuntry_nm}")
                        continue
                    Dataa[Cuntry_nm][Stat_nm] = []
                    while True:
                        City_ans = input(f"Add city in {Stat_nm}? y/n = ")
                        if City_ans == 'n':
                            break
                        elif City_ans != 'y':
                            print("not correct choice")
                            continue
                        else:
                            City_nm = input("City name: ")
                            if City_nm in Dataa[Cuntry_nm][Stat_nm]:
                                print("Already exist, try other name.")
                                continue
                            Dataa[Cuntry_nm][Stat_nm].append(City_nm)


csv_data_out = []


def dicttolist(dictt):
    """
    Convert dictt to list for csv write
    """
    if not dictt:
        print("No data found.")
        return
    for Cntry in dictt:
        if dictt[Cntry] == {}:
            row = [Cntry, "", ""]
            csv_data_out.append(row)
            continue
        citflg, stflg = 1, 1
        for st in dictt[Cntry]:
            if stflg == 1:
                row = [Cntry, st]
                stflg += 1
            else:
                row = ["", st]
            if not dictt[Cntry][st]:
                row.append("")
                csv_data_out.append(row)
            else:
                for ct in dictt[Cntry][st]:
                    if citflg == 1:
                        row.append(ct)
                        citflg += 1
                        csv_data_out.append(row)
                    else:
                        csv_data_out.append(["", "", ct])
                citflg = 1


Dataa = {}

while True:
    chs = input("\nmake from fix data = inbuild\nmake new data = new\nWhat u want: ")
    match chs:
        case "inbuild":
            dicttolist({'india': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]},
                        'Pak': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]}})
            break
        case "new":
            creet()
            dicttolist(Dataa)
            break
        case _:
            print("Plz give correct opt")

with open("output.csv", 'a', newline='') as f:
    wr = csv.writer(f)
    for dt in csv_data_out:
        wr.writerow(dt)

print(csv_data_out)


