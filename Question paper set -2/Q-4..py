employees = {
    'Robert Downey': {
        'designation': 'Project Manager',
        'experience': None,
        'team': {
            'Mark': {'designation': 'TL', 'experience': 8.0, 'manager': 'Robert Downey'},
            'Samuel': {'designation': 'TL', 'experience': 8.0, 'manager': 'Robert Downey'},
            'Paul': {'designation': 'TL', 'experience': 8.0, 'manager': 'Robert Downey'},
            'Tom': {'designation': 'TL', 'experience': 8.0, 'manager': 'Robert Downey'},
        }
    },
    'Anne Hathaway': {
        'designation': 'Project Manager',
        'experience': None,
        'team': {
            'Chris': {'designation': 'TL', 'experience': 5.0, 'manager': 'Anne Hathaway'},
            'Pratt': {'designation': 'TL', 'experience': 5.0, 'manager': 'Anne Hathaway'},
            'Emma': {'designation': 'TL', 'experience': 5.0, 'manager': 'Anne Hathaway'},
            'Will': {'designation': 'TL', 'experience': 5.0, 'manager': 'Anne Hathaway'},
            'Smith': {'designation': 'TL', 'experience': 5.0, 'manager': 'Anne Hathaway'},
        }
    },
    'Unassigned': {
        'designation': 'Unassigned',
        'experience': None,
        'team': {}
    },
}

employees['Anne Hathaway']['team']['Chris']['team'] = {
    'James': {'designation': 'TL', 'experience': None, 'manager': 'Chris'}
}
employees['Anne Hathaway']['team']['Chris']['team']['James']['team'] = {
    'Jennifer': {'designation': 'Senior Developer', 'experience': 3.8, 'manager': 'James'},
    'Scott': {'designation': 'Senior Developer', 'experience': 3.8, 'manager': 'James'},
    'Sophie': {'designation': 'Senior Developer', 'experience': 3.8, 'manager': 'James'}
}
employees['Robert Downey']['team']['Paul']['team'] = {
    'Fergal': {'designation': 'Senior Developer', 'experience': 4.5, 'mentor': 'Paul'}
}
employees['Anne Hathaway']['team']['Will']['team'] = {
    'Edge': {'designation': 'Senior Developer', 'experience': 3.0, 'manager': 'Will'},
    'Ryan': {'designation': 'Senior Developer', 'experience': 3.5, 'manager': 'Will'}
}
employees['Robert Downey']['team']['Tom']['team'] = {
    'Jerry': {'designation': 'Junior Developer', 'experience': 1.5, 'mentor': 'Tom'},
    'John': {'designation': 'Junior Developer', 'experience': 1.6, 'mentor': 'Tom'}
}
employees['Robert Downey']['team']['Mark']['team'] = {
    'Leonardo': {'designation': 'Junior Developer', 'experience': 1.0, 'mentor': 'Mark'},
    'Alexandra': {'designation': 'Junior Developer', 'experience': 1.0, 'mentor': 'Mark'}
}

employees['Anne Hathaway']['team']['Smith']['team'] = {
    'Walker': {'designation': 'Senior Developer', 'experience': 2.7, 'manager': 'Smith'},
    'Diana': {'designation': 'Senior Developer', 'experience': 2.7, 'manager': 'Smith'}
}


def find_employees_by_experience(employee_dict, min_exp):
    for emp_name, emp_data in employee_dict.items():
        if isinstance(emp_data, dict):
            if 'experience' in emp_data and emp_data['experience'] is not None and emp_data['experience'] > min_exp:
                print(f"{emp_name}: {emp_data['experience']} years of experience")
            if 'team' in emp_data and isinstance(emp_data['team'], dict):
                find_employees_by_experience(emp_data['team'], min_exp)


print("\nEmployees with more than 4 years of experience:")
find_employees_by_experience(employees, 4)


def update_experience(employee_dict):
    for emp_name, emp_data in employee_dict.items():
        if isinstance(emp_data, dict):
            if 'experience' in emp_data and emp_data['experience'] is not None and 3.5 < emp_data['experience'] < 4.5:
                emp_data['experience'] = 4.6
            if 'team' in emp_data and isinstance(emp_data['team'], dict):
                update_experience(emp_data['team'])


update_experience(employees)
print("\nUpdated employee dictionary after experience update:")
print(employees)


def display_tl_experience(employee_dict):
    for emp_name, emp_data in employee_dict.items():
        if isinstance(emp_data, dict):
            if 'designation' in emp_data and emp_data['designation'] == 'TL':
                experience = emp_data.get('experience', 'N/A')
                if experience is None:
                    experience = 'N/A'
                print(f"{emp_name} (TL): {experience} years")
            if 'team' in emp_data and isinstance(emp_data['team'], dict):
                display_tl_experience(emp_data['team'])


print("\nTeam Leaders with their experience:")
display_tl_experience(employees)
