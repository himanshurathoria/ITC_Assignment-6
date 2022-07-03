class Student:
    pass
class Marks:
    pass
himanshu=Student()
a_grade=Marks()
print("To check whether they are instances of said classes or not:")
print(isinstance(himanshu,Student))
print(isinstance(himanshu,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))