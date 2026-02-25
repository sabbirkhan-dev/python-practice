class Student:
    school = "Hatiara High School"
    def instance_method(self):
        print("Instance Method", self.school)

    @classmethod                # @ is a decorator
    def class_method(cls):
        print("Class method", cls.school)
        
    @staticmethod               # @ is a decorator
    def static_method():
        print("Static method")
        
        
# object call
s1 = Student()

s1.instance_method()
Student.class_method()
Student.static_method()
