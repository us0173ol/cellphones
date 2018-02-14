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
        for emp in self.employees:
            # print(emp)
            if emp.id == employee.id:
                raise PhoneError("Employee ID: {} already exists, can't duplicate entry".format(employee.id))

        self.employees.append(employee)


    def add_phone(self, phone):
        for phone_already_in_list in self.phones:
            if phone_already_in_list.id == phone.id:
                raise PhoneError("Cannot add phone, ID: {} currently exists.".format(phone.id))

        self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
        for phone in self.phones:
            if phone.id == phone_id:
                if phone.employee_id == employee.id:
                    print("Phone ID: {} already assigned to {}. ".format(phone.id, employee.name))
                    return
                elif phone.is_assigned():
                    raise PhoneError('The phone is already assigned to {}'.format(phone.employee_id))

            if phone.employee_id == employee.id:
                raise PhoneError("Employee {} already has a phone".format(employee.name))

        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(employee.id)
                return

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list
        if employee not in self.employees:
            raise PhoneError("Employee doesn't exist. ")
        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass
