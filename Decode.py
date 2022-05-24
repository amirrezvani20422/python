class Entery:
        firstname = ""
        lastname = ""
        personnal_ID = ""
   
        def __init__(self, firstname, lastname, personnal_ID):
            self.firstname = firstname
            self.lastname = lastname
            self.personnal_ID = personnal_ID
   
        def GetFullName(self):
            return self.firstname + " " + self.lastname
   
        def GetId(self):
           return self.personnal_ID
   
   
Firstname = input("Enter Firstname: ")
Lastname = input("Enter Lastname: ")
Personnal_ID = input("Enter Personnal_ID: ")
person =Entery(Firstname, Lastname, Personnal_ID)
print('''
   
    Help
    1 - Show Full name
    2 - Show Personnal Id
    3 - Exit
     ''')
brake=False
while brake ==False:
        entry = input("enter a number: ")
   
        if entry == "1":
            print(person.GetFullName())
        if entry == "2":
            print(person.GetId())
        if entry == "3":
                print('Exited')
                brake = True