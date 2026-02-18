
employee_id = {
    12345:{ "id": 12345,
           "name": "Sabbir",
           "department": "Admin"
    },
    23456:{
        "id": 23456,
        "name": "Tabbir",
        "department": "HR"
    }
}

def get_emp_form_dict_id (id):
    return employee_id.get(id)

print(get_emp_form_dict_id(23456))