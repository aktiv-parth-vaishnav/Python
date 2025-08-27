import xlwt
import xlrd

def action_create():
    global data
    while True:
        country = input("you wnt add cuntry? y/n = ")
        if country == 'n':
            if not data:
                pass
            else:
                print("result data: ")
            return
        elif country != 'y':
            print(" worng choise !!!")
            continue
        else:
            country_name = input("give country name: ")
            if country_name in data:
                print("alrdy exist. try new or delet first")
                continue
            data[country_name] = {}
            while True:
                state_ask = input(f"Add state in {country_name}? y/n = ")
                if state_ask == 'n':
                    break
                elif state_ask != 'y':
                    print("Wrong choise !!!")
                    continue
                else:
                    state_name = input("give state name: ")
                    if state_name in data[country_name]:
                        print(f"{state_name} alrdy in {country_name}")
                        continue
                    data[country_name][state_name] = []
                    while True:
                        city = input(f"Add city in {state_name}? y/n = ")
                        if city == 'n':
                            break
                        elif city != 'y':
                            print("Wrong choise !!!")
                            continue
                        else:
                            city_name = input("city name plz: ")
                            if city_name in data[country_name][state_name]:
                                print("Exist already !!.")
                                continue
                            data[country_name][state_name].append(city_name)
csv_out = []


def tolist(dict):
    """
    convert data which enter by input in form of dict to list to write in xlsx format
    state_line city_line indicate line it means after enter one value is there any other
    state and city it moves to the new line
    """
    if not dict:
        print("No data...")
        return
    for idx, ctry in enumerate(dict):
        # add new line when new country add 
        if idx > 0:
            csv_out.append(["", "", ""])

        if dict[ctry] == {}:
            one = [ctry, "", ""]
            csv_out.append(one)
            continue
       ## staring line 
        state_line, city_line = 1, 1
        for st in dict[ctry]:
            if state_line == 1:
                one = [ctry, st]
                state_line += 1
            else:
                one = ["", st]
            if not dict[ctry][st]:
                one.append("")
                csv_out.append(one)
            else:
                for ct in dict[ctry][st]:
                    if city_line == 1:
                        one.append(ct)
                        city_line += 1
                        csv_out.append(one)
                    else:
                        csv_out.append(["", "", ct])
                city_line = 1


data = {} ## final dictory which collect the data form user input

while True:
    chs = input("\nold data = inbuild\nnew data = new\nchoos what you want(inbuild/new)? ")
    match chs:
        case "inbuild":
            tolist({'india': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]},
                    'Pak': {"Sindh": ['Karachi'], 'Punjab': ["Lahore", "Multan"]}})
            break
        case "new":
            action_create()
            tolist(data)
            break
        case _:
            print("Plz write correct opt")

book = xlwt.Workbook()
sh = book.add_sheet("Sheet1")
style_bold = xlwt.easyxf('font: bold on')

# Apply bold style to headers
sh.write(0, 0, "Country", style_bold)
sh.write(0, 1, "State", style_bold)
sh.write(0, 2, "City", style_bold)

# Write data rows (shifted by +1 because header is row 0)
for r in range(len(csv_out)):
    for c in range(len(csv_out[r])):
        sh.write(r + 1, c, csv_out[r][c])

xl_file = "data_file.xls"
book.save(xl_file)
print(f"{xl_file} saved done.")

# Read xlsx file
try:
    bk = xlrd.open_workbook(xl_file)
    sh = bk.sheet_by_index(0)

    print("Reading file...")
    for r in range(sh.nrows):
        for c in range(sh.ncols):
            print(f"R{r}, C{c} => {sh.cell_value(rowx=r, colx=c)}")

except xlrd.biffh.XLRDError as err:
    print("error: ", err)
