class Person:
    moods = ("Happy","Tired","Lazy")
    def __init__(self,name,maney,mood,healthRate):
        self.name = name
        self.maney = maney
        self.mode = mood
        self.healthRate = healthRate
#  sleep (hours): - Method in Person Class (7 hours →happy, <7 hours →tired, >7 hours →Lazy)
    def sleep(hours):
        if hours == 7:
            return Person.moods[0]
        elif hours > 7:
            return Person.moods[1]
        else:
            return Person.moods[2]
# - Method in Person Class (3 meals →100% hth , 2 meals →75% , 1 meal →50%
    def eat(meals):
        if meals == 3:
            return "100%"
        elif meals == 2:
            return "75%"
        elif meals == 1:
            return "50%"
        else: return "meals should be 3,2 or 1"
#  Method in Person Class (1 item →decrease money 10 L.E
    def buy(self,items):
        self.maney -= items * 10
        return "buing done successfully"
    
        
    
class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, email, salary, distanceToWalk, carObj):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.email = email
        self.salary = salary
        self.distanceToWalk = distanceToWalk
        self.carObj = carObj
# Method in Employee Class (8 hours→happy, >8 hours →tired,<8 hours →Lazy)
    def work(hours):
        if hours == 8:
            return Employee.moods[0]
        elif hours > 8:
            return Employee.moods[1]
        else:
            return Employee.moods[2]
    def drive():
        pass
    def refuel():
        pass
    def send_mail():
        pass
"""- send_mail(to, subject, msg, receiver_name): (optional)
- Create Email File like the next page specification (Email Composer)
- salary Property: must be 1000 or more.
- email Property: must be valid.
- healthRate Property: must be between 0 to 100.
- There is moods class variable which is tuple of happy, tired and lazy
"""

class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
        
    def run():
        pass
    def stop():
        pass