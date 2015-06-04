# Using Inheritance and Polymorphism

class myActions:
    def sing(self): return self.strings['sing']
    def covering(self): return self.strings['covering']
    def speak(self): return self.strings['speak']
    def fur(self): return self.strings['fur']
    
class Dog(myActions):
    strings = dict(
        sing = "AAooohohhh!"
        covering = "The dog har hair that covers it"
        speak = "The dog cannot bark!"
        fur = "The dog usually will not have fur"
    )
    
class Person(myActions):
    strings = dict(
        sing = "**sings song**"
        covering = "skin"
        speak = "Hello World!"
        fur = "Humans do not have fur!"
    )
    
class bird(myActions):
    strings = dict(
        sing = "chirp chirp!"
        covering = "The bird is covered in feathers"
        speak = "The bird cannot speak!"
        fur = "Birds do not have fur"
    )

def doghouse(dog):
    print(dog.sing())
    print(dog.covering())
    print(dog.speak())
    print(dog.fur())

def forest(bird):
    print(bird.sing())
    print(bird.covering())
    print(bird.speak())
    print(bird.fur())
    
def house(person):
    print(person.sing())
    print(person.covering())
    print(person.speak())
    print(person.fur())
    
def main():
    tweetie = Bird()
    trey = Person()
    bingo = Dog()
    
    print("In the Forest: ")
    for o in (tweetie, trey, bingo):
        forest(o)
    
    print("In the Doghouse: ")
    for o in (tweetie, trey, bingo):
        doghouse(o)

if __name__ == "__main__": main()