import random
import os
run = True


#GUI for the game
def Start(Answer, wrong_guess):
  print("                   ")
  print("                   ")
  print("                   ")
  print("                   ")
  print("                   ")
  print("                   ")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)

def Seocnd(Answer, wrong_guess):
  print("                   ")
  print("                   ")
  print("                   ")
  print("                   ")
  print("                   ")
  print("___________________")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)

def third(Answer, wrong_guess):
  print("                   ")
  print("   /               ")
  print("  |                ")
  print("  |                ")
  print("  |                ")
  print("__|________________")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)

def third(Answer, wrong_guess):
  print("    ________       ")
  print("   /      |        ")
  print("  |                ")
  print("  |                ")
  print("  |                ")
  print("__|________________")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)

def four(Answer, wrong_guess):
  print("    ________       ")
  print("   /      |        ")
  print("  |       0        ")
  print("  |                ")
  print("  |                ")
  print("__|________________")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)

def five(Answer, wrong_guess):
  print("    ________       ")
  print("   /      |        ")
  print("  |       0        ")
  print("  |      \|/       ")
  print("  |      / \       ")
  print("__|________________")
  print("\n Guess the word\n",Answer)
  print("\nWrong \n", wrong_guess)



#Cleans screen ready for new games
os.system('clear')


#Game stats
Run_through = 0 #Used to make the code check each letter
Attemps = 5 #Give the user limited attemps to get the right answer
word_list = ["ted","ford","jazz","steam","apple"] #Words the game can choice form
Answer = [] #What the acutal in game ansewer is
Score = 0 #Used to detect if winnig Score is entered
wrong_guess = [] #answer already submited

#Bot word choice
word = random.choice(word_list)

#Creates the word hint
for i in range(len(word)):
  Answer.append('_')
  

while run == True:
#Game play
  for i in range(len(word)):

    
    #GUI
    if Attemps == 5:
      Start(Answer,wrong_guess)
    elif Attemps == 4:
      os.system('clear')
      Seocnd(Answer,wrong_guess)
    elif Attemps == 3:
      os.system('clear')
      third(Answer,wrong_guess)
    elif Attemps == 2:
      os.system('clear')
      four(Answer,wrong_guess)
    elif Attemps == 1:
      os.system('clear')
      five(Answer,wrong_guess)
      
    Player_inpupt = input("Please guess a letter\n")
    Player_guess = Player_inpupt.lower()
    if Player_guess == word[Run_through]:
      
      #Add the right ansewer to the list
      Answer.insert(Run_through, Player_guess)
      #Finds the loaction of the desired - to remove
      Clear_up = Run_through + 1
      #Removes it
      Answer.pop(Clear_up)
      print(Answer)
      #Lets the player know they where right
      print("is in there")
      Run_through = Run_through + 1
      Score = Score + 1
      os.system('clear')
    
    
    #If the guess is wrongs pass it on
    elif Player_guess != word[Run_through]:
      Run_through = Run_through + 1
      wrong_guess.append(Player_guess)
      Attemps = Attemps -1
    
    
    #Sets the check back to Zero ready for next guess
    if Run_through == len(word):
      Run_through = 0
     

    if Score == int(len(word)):
      os.system('clear')
      print("You win the word was", word)
      run = False
      break

    if Attemps == 0:
      os.system('clear')
      print("Game over")
      run = False
      break
