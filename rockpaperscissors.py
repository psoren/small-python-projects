from random import randint

playerScore = 0
compScore = 0

def startup():

    global player
    global computer
    print('Would you like to be Rock (r), Paper(p), or Scissors(s)?')
    player = input().lower()
    while(player != "r" and player != "s" and player != "p"):
        print('Please enter r, p, or s.')
        player = input().lower()

    compPicker = ["r","s","p"]
    computer = compPicker[randint(0,2)]

def game(player, comp):
    global playerScore
    global compScore
    
    if(player == comp):
        print("It's a tie!")
        return
    if(player == "r"):
        if comp == "s":
            print("You win! The computer picked scissors!")
            playerScore += 1
            return
        print('You lose! The computer picked paper!')
        compScore += 1

    elif(player == "p"):
        if comp == "s":
            print("You lose! The computer picked scissors!")
            compScore += 1
            return
        print('You win! The computer picked rock!')
        playerScore += 1
        return

    elif(player == "s"):
        if comp == "p":
            print("You win! The computer picked paper!")
            playerScore += 1
            return
        print('You lose! The computer picked rock!')
        compScore += 1

def willExit():
    print("If you want to quit, press q. Otherwise, press any other key.\n")
    willQuit = input().lower()
    if willQuit == 'q':
        return True
    return False

def printScore():
    global playerScore
    global compScore
    
    print('Your score was ' + str(playerScore) + '.')
    print("The computer's score was "+ str(compScore)+ '.')

print('\nHello,\nwelcome to Rock, Paper, Scissors.\n')    
keepPlaying = True
startup()
game(player, computer)
while True:
 
    if willExit():
         printScore()
         break

    startup()
    game(player, computer)
