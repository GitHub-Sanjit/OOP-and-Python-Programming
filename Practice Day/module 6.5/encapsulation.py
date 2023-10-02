"""
Encapsulation:
Encapsulation is one of the four fundamental OOP principles that involves bundling data (attributes) and the methods (functions) that operate on that data into a single unit called a class. It helps in data hiding and protection by restricting direct access to an object's internal state. Access to attributes is controlled through access modifiers.

Access Modifiers: These are keywords that define the scope or visibility of class members (attributes and methods). In Python, there are three common access modifiers:
public: Members are accessible from anywhere (default).
protected: Members are accessible within the class and its subclasses (denoted by a single underscore prefix, e.g., _variable).
private: Members are accessible only within the class (denoted by a double underscore prefix, e.g., __variable).
Example:
"""
class Employee:
    def __init__(self, name, _salary, __id):
        self.name = name
        self._salary = _salary
        self.__id = __id


emp = Employee("John", 50000, 12345)

print(emp.name)  # Accessing a public attribute
print(emp._salary)  # Accessing a protected attribute (not recommended)
print(emp.__id)  # Accessing a private attribute (will raise an error)

"""
     It's important to note that even though Python has these access modifiers, it relies on naming conventions and doesn't enforce strict encapsulation like some other languages (e.g., Java). Developers are expected to follow naming conventions and respect the intended access levels.   
        
"""
