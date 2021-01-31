class School1():
    def _init_(self,name,surname,age,email,number,schedule):
        print("School1 class function")
        self.name=name
        self.surname=surname
        self.email=email
        self.number=number
        self.schedule=schedule



    def enter(self):
        print("You enter to system")

    def exit(self):
        print("You enter from system")



class Teachers(School1):
    pass
class Students(School1):
    pass
class Workers(School1):
    pass




class School2():
    def _init_ (self,books,brands_of_computers,activities,rooms):
        print("School2 class function")
        self.books=books
        self.brands_of_computers=brands_of_computers
        self.activities=activities
        self.rooms=rooms
       


    def enter(self):
        print("You enter to system")

    def exit(self):
        print("You enter from system")



class Departments(School2):
    pass
class Faculties(School2):
    pass
    
class School3():
    def _init_(self,equipments,degrees_of_attendance,type_of_assesment):
        print("School3 class function")
        self.equipments=equipments
        self.degrees_of_attendance=degrees_of_attendance
        self.type_of_assesment=type_of_assesment
      
       


    def enter(self):
        print("You enter to system")

    def exit(self):
        print("You enter from system")



class HighScools(School3):
    pass
class SecondarySchool(School3):
    pass
        
        
   
    
