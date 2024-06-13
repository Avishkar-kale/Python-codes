# Duck typing is a programming concept where the type or class of an object is determined by its behavior.
# (methods and properties) rather than its explicit type.


class Duck:
    def swim(self):
        print('i am duck and i can swim')
    def speak(self):
        print('I can speak Quack Quack')

class Dog:
    def swim(self):
        print('I am dog and i can speak')
    def speak(self):
        print('I am dog and i speak like')

def Display(duck):
    duck.swim()
    duck.speak()
    print('information displayed')

d=Duck()
print(Display(d))
dog=Dog()
print(Display(dog))
