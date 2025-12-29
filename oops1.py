# initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("started executing attributes/data.")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data has been initiated.")
    # defining a method
    def travel(self, destination):
        print("This travel method was called manually.")
        print(f"employee is travelling to {destination}")

# create an object/instance of the class
sam = employee()

#printing an attribute
#print(sam.salary)

#calling a method
# sam.travel("kerala")
print(type(sam))