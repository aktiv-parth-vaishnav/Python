import xlwt
import xlrd


def kreeat():
    """
    This funtion only creat data and store in Dtaa var.
    Countr, Stat, Cit: Ask user if want to add or not

    """
    global Dtaa
    while True:
        Countr_ask = input("you wnt add cuntry? y/n = ")
        if Countr_ask == 'n':
            if not Dtaa:
                pass
            else:
                print("ur Data is ready: ")
            return
        elif Countr_ask != 'y':
            print("Wrong choise")
            continue
        else:
            Cntr_name = input("give country name: ")
            if Cntr_name in Dtaa:
                print("Alrdy exist. try new or delet first")
                continue
            Dtaa[Cntr_name] = {}
            while True:
                Stat_ask = input(f"Add state in {Cntr_name}? y/n = ")
                if Stat_ask == 'n':
                    break
                elif Stat_ask != 'y':
                    print("Wrong choise")
                    continue
                else:
                    St_name = input("give state name: ")
                    if St_name in Dtaa[Cntr_name]:
                        print(f"{St_name} alrdy in {Cntr_name}")
                        continue
                    Dtaa[Cntr_name][St_name] = []
                    while True:
                        Cit_ask = input(f"Add city in {St_name}? y/n = ")
                        if Cit_ask == 'n':
                            break
                        elif Cit_ask != 'y':
                            print("Wrong choise")
                            continue
                        else:
                            Ct_name = input("city name plz: ")
                            if Ct_name in Dtaa[Cntr_name][St_name]:
                                print("Exist already.")
                                continue
                            Dtaa[Cntr_name][St_name].append(Ct_name)


csv_out = []


def tolist(dicti):
    """
    Convert dict data to list for xls write
    """
    if not dicti:
        print("No data...")
        return
    for ctry in dicti:
        if dicti[ctry] == {}:
            one = [ctry, "", ""]
            csv_out.append(one)
            continue
        st_flag, ct_flag = 1, 1
        for st in dicti[ctry]:
            if st_flag == 1:
                one = [ctry, st]
                st_flag += 1
            else:
                one = ["", st]
            if not dicti[ctry][st]:
                one.append("")
                csv_out.append(one)
            else:
                for ct in dicti[ctry][st]:
                    if ct_flag == 1:
                        one.append(ct)
                        ct_flag += 1
                        csv_out.append(one)
                    else:
                        csv_out.append(["", "", ct])
                ct_flag = 1


Dtaa = {}

while True:
    chs = input("\nold data = inbuild\nnew data = new\nU choos what? ")
    match chs:
        case "inbuild":
            tolist({'india': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]},
                    'Pak': {"Guj": ['Ahmedabad', "Gandhinagar"], 'Raj': ["Udaipur", "Jodhpur"]}})
            break
        case "new":
            kreeat()
            tolist(Dtaa)
            break
        case _:
            print("Plz write correct opt")

# create xl file
book = xlwt.Workbook()
sh = book.add_sheet("Sheet1")
for r in range(len(csv_out)):
    for c in range(len(csv_out[r])):
        sh.write(r, c, csv_out[r][c])
xl_file = "data_file.xls"
book.save(xl_file)
print(f"{xl_file} saved done.")

# Read xl file
try:
    bk = xlrd.open_workbook(xl_file)
    sh = bk.sheet_by_index(0)

    print("Reading file...")
    for r in range(sh.nrows):
        for c in range(sh.ncols):
            print(f"R{r}, C{c} => {sh.cell_value(rowx=r, colx=c)}")

except xlrd.biffh.XLRDError as err:
    print("error: ", err)
