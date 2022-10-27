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
        super().showDetails()
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
        super().showDetails()
        print("Holidays Left: "+ str(self.holiday))
        print("Trips Left: "+ str(self.trips))


a1= Private()
a1.fillDetails("Arijit Ghosh","M",20, "B+","Unmarried")
a1.member("Google","G-2939","UK","SDE","100K")
a1.showDetails()
a1.claimBonus(100)
a1.claimSwag()
a1.claimSwag()
print("\n")
a1.showDetails()
print("\n")
a2=Government()
a2.fillDetails("Devika Ghosh","F",20,"B+","Unmarried")
a2.member("Canary Bank","C-48392","Kolkata","Officer","60K")
print("\n")
a2.showDetails()
a2.claimHoliday()
a2.claimTrip()
print("\n")
a2.showDetails()