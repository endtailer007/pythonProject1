# class provides a blueprint or a template,where as object is an instance of the class
# creation of object object_name=class_name() or this is called as class instantiation
# Python does not require the new operator to create an object
# object_name.class_membername() access class data
# when we use __init__ method is a class constructor it is automatically executed when an object of a class is created.It is uded to initialize data members of the class
class student():
    rollno=0
    name=""
    degree=0
    aggreggate=0
    def __init__(self,degree,name):
        #'''This method is used for initialisation of the object'''
        self.degree=degree
        self.name=name
#This accepts input of student data
    def setstudentdetails(self):
       self.rollno=input("Enter student rollno: ")
       #self.name=input("Enter student name: ")
       #self.degree=input("Enter student branch: ")
       self.aggreggate=float(input("Enter student cgpa: "))
#This method displays the details of the  student
    def getstudentdetails(self):
        print("Rollno of the student is ",self.rollno)
        print("Name of the student is ",self.name)
        print(self.name,"studies",self.degree)
        print("aggreggate of student is ",self.aggreggate)
student1=student("BE","Sooraj")
student1.setstudentdetails()
student1.getstudentdetails()

