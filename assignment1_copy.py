class Human:
    def fillDetails(self,name, gender, age, blood, marital):
        self.name=name
        self.gender=gender
        self.age=age
        self.blood=blood
        self.marital=marital

class Employee(Human):
    def member(self, company, id, location, role, salary):
        self.company=company
        self.id=id
        self.location=location
        self.role=role
        self.salary=salary

class Private(Employee):

    def __init__(self):
        print("Private Employee Created.")

    bonus=100000
    swags=10

    def claimBonus(self,percent):
        print("Bonus Claimed:",self.bonus*(percent/100))
        self.bonus= self.bonus-self.bonus*(percent/100)
    def claimSwag(self):
        self.swags= self.swags-1
    
    def showDetails(self):
        print("Name: "+ self.name)
        print("Gender: "+ self.gender)
        print("Age: "+ str(self.age))
        print("Blood Group: "+ self.blood)
        print("Marital Status: "+ self.marital)
        print("Company Name: "+ self.company)
        print("Employee ID: "+ self.id)
        print("Location: "+ self.location)
        print("Role: "+ self.role)
        print("Salary: "+ self.salary)
        print("Bonuses Recieved: "+ str(self.bonus))
        print("Swags Left: "+ str(self.swags))


class Government(Employee):

    holiday=10
    trips=10

    def __init__(self):
        print("Government Employee Created")

    def claimHoliday(self):
        self.holiday=self.holiday-1

    def claimTrip(self):
        self.trips=self.trips-1
    
    def showDetails(self):
        print("Name: "+ self.name)
        print("Gender: "+ self.gender)
        print("Age: "+ str(self.age))
        print("Blood Group: "+ self.blood)
        print("Marital Status: "+ self.marital)
        print("Company Name: "+ self.company)
        print("Employee ID: "+ self.id)
        print("Location: "+ self.location)
        print("Role: "+ self.role)
        print("Salary: "+ self.salary)
        print("Holidays Left: "+ str(self.holiday))
        print("Trips Left: "+ str(self.trips))


