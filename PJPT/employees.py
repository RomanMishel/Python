class employees:

    def __init__(self, name, department, role, salary, years_employed):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
        self.years = years_employed

    def eligable_for_retirement(self):
        if self.years >= 20:
            return True
        else:
            return False
        