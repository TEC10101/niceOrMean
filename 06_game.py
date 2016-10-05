# Python v 2.7.12
# author: tyler corum
# purpose: the tech academy python course drill 6 of 63

#def start():
#    print("Hello {}".format(get_name()))
#def get_name():
#    name = raw_input("What is your name? ")
#    return name
#if __name__ == "__main__":
#    start()


#def start():
#    fName = "Sarah"
#    lName = "Connor"
#    age = 28
#    gender = "Female"
#    getInfo(fName,lName,age,gender)

#def getInfo(fName,lName,age,gender):
#    print("My name is {} {}.  I am {} year old {}.".format(fName,lName,age,gender))



#if __name__ == "__main__":
#    start()


def start(nice=0,mean=0,name=""):
    #get user's name
    name = describeGame(name)
    nice,mean,name = niceMean(nice,mean,name)


def describeGame(name):
    """
    check if this is new game or not
    if it is new get user's name
    if it is not a new game thank for playing
    again and continue
    """
    if name != "": #meaning if we do not already have this user's name, then they are a new player and we need to gt their name
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize() #takes whatever they give us gives the first letters capital
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.  \nYou can be nice or mean.")
                    print("At the end of the game your fate will be influenced from your actions.")
                    stop = False
    return name


def niceMean(nice,mean,name):
    stop = True
    while stop:
        showScore(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a convo.\nWill you be nice or mean? n/m:").lower() #set input to lowercase
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 vars to the score()




def showScore(nice,mean,name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    #score func is being passed the values stored within the 3 vars
    if nice > 5:
        win(nice,mean,name)
    if mean > 5:
        lose(nice,mean,name)
    else:
        niceMean(nice,mean,name)



def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you now live in a palace!".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nToo bad, game over! \n{}, you live in a van by the right, wretched and alone!".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you later alligator!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for YES and 'n' for NO...")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)



                  
if __name__ == "__main__":
    start()
