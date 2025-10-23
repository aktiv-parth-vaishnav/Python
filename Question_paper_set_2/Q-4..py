company = {
    "Robert Downey": {
        "designation": "Project Manager",
        "team_leads": {
            "Mark": {
                "designation": "TL",
                "experience": 8,
                "developers": {
                    "Leonardo": {"designation": "Junior Developer", "experience": 1},
                    "Alexandra": {"designation": "Junior Developer", "experience": 1},
                }
            },
            "Samuel": {"designation": "TL", "experience": 8, "developers": {}},
            "Paul": {
                "designation": "TL",
                "experience": 8,
                "developers": {
                    "Fergal": {"designation": "Senior Developer", "experience": 4.5, "mentor": "Paul"}
                }
            },
            "Tom": {
                "designation": "TL",
                "experience": 8,
                "developers": {
                    "Jerry": {"designation": "Junior Developer", "experience": 1.5, "mentor": "Tom"},
                    "John": {"designation": "Junior Developer", "experience": 1.6, "mentor": "Tom"},
                }
            }
        }
    },
    "Anne Hathaway": {
        "designation": "Project Manager",
        "team_leads": {
            "Chris": {
                "designation": "TL",
                "experience": 5,
                "developers": {
                    "James": {
                        "designation": "TL",
                        "experience": None,
                        "developers": {
                            "Jennifer": {"designation": "Senior Developer", "experience": 3.8, "manager": "James"},
                            "Scott": {"designation": "Senior Developer", "experience": 3.8, "manager": "James"},
                            "Sophie": {"designation": "Senior Developer", "experience": 3.8, "manager": "James"},
                        }
                    }
                }
            },
            "Pratt": {"designation": "TL", "experience": 5, "developers": {}},
            "Emma": {"designation": "TL", "experience": 5, "developers": {}},
            "Will": {
                "designation": "TL",
                "experience": 5,
                "developers": {
                    "Edge": {"designation": "Senior Developer", "experience": 3, "manager": "Will"},
                    "Ryan": {"designation": "Senior Developer", "experience": 3.5, "manager": "Will"},
                }
            },
            "Smith": {
                "designation": "TL",
                "experience": 5,
                "developers": {
                    "Walker": {"designation": "Senior Developer", "experience": 2.7, "manager": "Smith"},
                    "Diana": {"designation": "Senior Developer", "experience": 2.7, "manager": "Smith"},
                }
            },
        }
    }
}


def get_all_employees(pm_name):
    """
    display all employees' names for the given project manager

    return none
    """
    employees = []
    pm = company.get(pm_name)
    if pm:
        for tl_name, tl in pm["team_leads"].items():
            employees.append(tl_name)
            for dev_name in tl.get("developers", {}):
                employees.append(dev_name)
    print(f"All employees under Project Manager '{pm_name}': {employees}")


get_all_employees("Robert Downey")
get_all_employees("Anne Hathaway")


def experienced_employees():
    """
    show employees who have more than 4 year experience
    """
    names = []
    for pm in company.values():
        for tl in pm["team_leads"].values():
            if tl.get("experience") and tl["experience"] > 4:
                names.append(tl.get("designation") + " " + str(tl))
            for dev_name, dev in tl.get("developers", {}).items():
                if dev.get("experience") and dev["experience"] > 4:
                    names.append(dev_name)
    print(f"Employees with experience > 4 years: {names}")


experienced_employees()


def update_experience():
    """
     update experience with 4.6 whose experience is greater than 3.5 and less than 4.5 years

     return none
    """
    for pm in company.values():
        for tl in pm["team_leads"].values():
            if tl.get("experience") and 3.5 < tl["experience"] < 4.5:
                tl["experience"] = 4.6
            for dev in tl.get("developers", {}).values():
                if dev.get("experience") and 3.5 < dev["experience"] < 4.5:
                    dev["experience"] = 4.6
    print("Updated experience for employees with 3.5 < exp < 4.5 to 4.6")


update_experience()


def display_tl_experience():
    """
     display tl with their year of experience

     return none
    """
    tl_list = {}
    for pm in company.values():
        for tl_name, tl in pm["team_leads"].items():
            tl_list[tl_name] = tl.get("experience", "N/A")
    print("Team Leads with their experience:", tl_list)


display_tl_experience()


def reassign_smith():
    """
     smith's employee  all his members to assigned to Ryan

    """
    anne = company["Anne Hathaway"]
    if "Smith" in anne["team_leads"]:
        smith_devs = anne["team_leads"]["Smith"]["developers"]
        if "Ryan" in anne["team_leads"]:
            anne["team_leads"]["Ryan"]["developers"].update(smith_devs)
        else:
            anne["team_leads"]["Ryan"] = {"designation": "TL", "experience": 3.5, "developers": smith_devs}
        del anne["team_leads"]["Smith"]
    print("Smith's team reassigned to Ryan")


reassign_smith()


def has_less_than_2_years():
    """
     check company if  employee who less than 2 years of experience

     return none
    """
    for pm in company.values():
        for tl in pm["team_leads"].values():
            if tl.get("experience") and tl["experience"] < 2:
                print("Yes, company has employee with less than 2 years of experience")
                return
            for dev in tl.get("developers", {}).values():
                if dev.get("experience") and dev["experience"] < 2:
                    print("Yes, company has employee with less than 2 years of experience")
                    return
    print("No employee has less than 2 years of experience")


has_less_than_2_years()


def check_edge_tl():
    """
    check whether edge is tl or not if not make him tl

    return none
    """
    for pm in company.values():
        for tl in pm["team_leads"].values():
            if "Edge" in tl.get("developers", {}):
                edge = tl["developers"].pop("Edge")
                pm["team_leads"]["Edge"] = {"designation": "TL", "experience": "N/A", "developers": {}}
                print("Edge is now promoted to TL")
                return
    print("Edge is already TL")


check_edge_tl()
