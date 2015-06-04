# Making a simple class

class Dog:
    def bark(self):
        print("Woof!")
    
    def howl(self):
        print("AAooohhhhhh!")
    
    def walk(self):
        print("Walk like a dog!")
    
def main():
    bingo = Dog()
    bingo.walk()
    bingo.howl()
    bingo.bark()
    
if __name__ == "__main__": main()
    