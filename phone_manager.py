# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        for employee in self.employees:
            if employee.id == employee.id:
                raise PhoneError("Employee %s already exists, can't duplicate entry" % employee_already_in_list)

        self.employees.append(employee)




    def add_phone(self, phone):
        for phone_already_in_list in self.phones:
            if phone_already_in_list.id == phone.id:
                raise PhoneError("Cannot add phone, ID currently exists.")

        self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.

        for phone in self.phones:
            if phone.id == phone_id and employee.id == None:
                phone.assign(employee.id)
                return
            if phone.id == phone_id:
                raise PhoneError("Phone already assigned to another employee. ")
            if phone.employee_id == employee.id and phone.id == phone_id:
                return
            if phone.employee_id == employee.id:
                raise PhoneError("Employee %s already has a phone" %employee.name)


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list
        if employee is None and employee.id is None:
            raise PhoneError("Employee doesn't exist")
        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass
