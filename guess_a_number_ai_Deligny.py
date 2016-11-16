# Guess-A-Number AI
#
# Eliot Deligny
# September 9, 2016

n = ['n','no','nope','nah','nein','harambe didnt die for this']
y = ['y','yes','yeah','yah','ya','sure','okay','alright']
cheeter = [-1,0,1]

print("╔═╗╦ ╦╔═╗╔═╗╔═╗  ╔═╗  ╔╗╔╦ ╦╔╦╗╔╗ ╔═╗╦═╗")
print("║ ╦║ ║║╣ ╚═╗╚═╗  ╠═╣  ║║║║ ║║║║╠╩╗║╣ ╠╦╝")
print("╚═╝╚═╝╚═╝╚═╝╚═╝  ╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═")
print("        Press Enter to continue         ")
input()

def play():

    yes = False
    print("I think I can guess a number that you are thinking of from a value to a value!")
    low = input("Insert your low value here ")
    low = int(low)
    high = input("Insert your high value here ")
    high = int(high)
    print("Think of a number from " + str(low) + " to " + str(high) + " and I will try to guess it.")
    input("Press Enter once you've thought of a number")
    guess = ((high + low) // 2)
    tries = 1
    print("Is it " + str(guess) + "? answer, 'yes', 'lower', or 'higher'")
    while yes == False:

        
        answer = input()

        guess = ((high + low) // 2)
        
        if answer.lower() in y:
            print()
            if tries == 1:
                print("I won, and it only took me " + str(tries) + " try!")
            else:
                print("I won, and it only took me " + str(tries) + " tries!")
            yes = True
        elif high - low in cheeter:
            print("HOLY SMOKES ARE YOU TRYING TO GIVE ME THE SLIP? IT'S " + str(guess) + " ISN'T IT?")
            print("It took me " + str(tries) + " tries!")
            yes = True
        elif answer.lower() == 'harambe didnt die for this':
            print("Oh dang u rite")
            yes = False
        elif answer.lower() == 'lower' or answer.lower() == 'l':
            high = guess - 1
            print()
            print("Is it " + str((low + high) // 2) + "?")
        elif answer.lower() == 'higher' or answer.lower() == 'h':
            low = guess + 1
            print()
            print("Is it " + str((low + high) // 2) + "?")
        else:
            print()
            print("Say 'lower','higher' or 'yes'")
            tries -= 1
        tries += 1
        


def play_again():

    while True:
        answer = input("Want to play again? ")

        if answer.lower() in n:
            return False
        elif answer.lower() in y:
            return True

        print("I'm not picking up what you're putting down..")

again = True

while again == True:
    play()
    again = play_again()

print("Bye!")
    
