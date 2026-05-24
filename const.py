# CONSTRUCTORS AND DECORATORS

# Constructors 

class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = person("Alice", 30)
person2 = person("Bob", 25)


person1.info()
person2.info()ṇ


# Decorators
def  greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning Everyone!")
        fx(*args, **kwargs)
        print("Have a nice day!")
    
    return mfx
@greet
def hello():
    print("Hello, World!")

def add(a,b):
    print(a + b)

hello()
add(5, 10)
