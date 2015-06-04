# Storing arguments

class myArgs:
    def printUser(self): return self.strings['user']
    def printPass(self): return self.strings['passWord']
    def printEmail(self): return self.strings['email']
    def printName(self): return self.strings['name']
    
class FirstUser(myArgs):
    strings = dict(
        user = "dpctrey",
        passWord = "bingo123",
        email = "dpctrey@gmail.com",
        name = "Dwight P. Christian III"
    )
    
class SecondUser(myArgs):
    strings = dict(
        user = "dchristian",
        passWord = "trey1234",
        email = "dchristian@gmail.com",
        name = "Dwight Patton Christian III"
    )
    
def on_the_site(variable):
    print(variable.printUser())
    print(variable.printPass())
    print(variable.printEmail())
    print(variable.printName())
    
def main():
    dwight = FirstUser()
    trey = SecondUser()
    
    print("The following users are registered: ")
    for i in (dwight, trey):
        on_the_site(i)
        
if __name__ == "__main__": main()