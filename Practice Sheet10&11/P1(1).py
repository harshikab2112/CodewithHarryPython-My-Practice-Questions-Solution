# Create a Class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self, id, name, designation, salary):
        self.id = id
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(
            f"Employee Details:\n"
            f"Company: {Programmer.company}\n"
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Designation: {self.designation}\n"
            f"Salary: ₹{self.salary:,}\n"
        )


Employee1 = Programmer(23, "Yamini", "Software Engineer", 2000000)
Employee2 = Programmer(101, "Rishabh", "Data Analyst", 1800000)
Employee1.display_info()
Employee2.display_info()
