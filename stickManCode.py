'''
Student Name: Amitva Pal
Game title: HangMan
Period: 6
Features of Game: Guessing Game
'''

import pygame, sys,random                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=480                                                   #Open and set window size
h=640                                                  #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Stickman")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):


def showMessage(words,  size, xValue,yValue,color, bg=None):
   font = pygame.font.SysFont("Consolas", size, True,False)
   text = font.render(words, True, color, bg)

   #centering the text, must get bounding box
   tbounds= text.get_rect()

   #center text in middle of screen
   tbounds.center= (xValue,yValue)  

   return text, tbounds


def wordDisplay():
   pygame.draw.rect(surface,BLACK,(w/4, 3*h/4, w/2, h/8),0)
   


def getMysteryWord():
   wordList = ["concatenation", "programming", "python", "function", "computer", "binary", "logic", "loop","statement"]
   return random.choice(wordList)

def isValidLetter(letter,used):
   if len(letter)!=1:
      print("Invalid letter entered")
      return False
   if letter>"z" or letter<"a":
      print("Invalid letter entered")
      return False
   if letter in used:
      print("You have alredy chosen this letter")
      return False
   return True


def updateUserWord(getMysteryWord,usedLetters):
   result = ""
   for ch in getMysteryWord:
      if ch in usedLetters:
         result+=ch
      else:
         result+="-"
   return result

def drawGallows():
   pygame.draw.rect(surface,BLACK,(w/4, 3*h/4, w/2, h/8),0)
   point=[(w/2, 3*h/4), (w/2, h/4), (3*w/4, h/4), (3*w/4, h/3)]
   pygame.draw.lines(surface, BLACK, False, point, 10)

   
def drawHead():
   pygame.draw.ellipse(surface, BLACK,(11*w/16, h/3, w/8, w/8),5)

def drawBody():
   pygame.draw.line(surface,BLACK ,[3*w/4, h/3+w/8], [3*w/4, 3*h/5],5)


def drawLArm():
   pygame.draw.line(surface, BLACK, [3*w/4, h/2], [11*w/16, 6.5*h/15],5)

def drawRArm():
   pygame.draw.line(surface, BLACK, [3*w/4, h/2], [13*w/16, 6.5*h/15],5)

def drawLLeg():
   pygame.draw.line(surface, BLACK, [.67*w, .7*h], [12*w/16, 9*h/15],5)

def drawRLeg():
   pygame.draw.line(surface,BLACK, [.84*w, .7*h], [12*w/16, 9*h/15],5)

def drawHangman(userMisses):
   drawGallows()
   if userMisses >= 1:
      drawHead()
   if userMisses >= 2:
      drawBody()
   if userMisses>=3:
      drawLArm()
   if userMisses>=4:
      drawRArm()
   if userMisses>=5:
      drawLLeg()
   if userMisses>=6:
      drawRLeg()
      
def drawScreen(userWord, userMisses, getMysteryWord,usedLetters ):
   drawHangman(userMisses)
   textImage, textBounds = showMessage(userWord, 24, w/2, h/9, BLACK)
   surface.blit(textImage, textBounds)
   usedText, usedBounds = showMessage(" ".join(usedLetters), 24, w/2, h/1.2, RED)
   surface.blit(usedText,usedBounds)
   mysteryWord = getMysteryWord()
   if userMisses==6:
      
      looseText,looseBounds = showMessage("You Lost", 30, w/2, h/2, BLUE)
      surface.blit(looseText,looseBounds)
      againText,againBounds = showMessage("Would you like to play again?(Press Enter to play)", 15, w/2, h/1.8, BLUE)
      surface.blit(againText, againBounds)
   elif userWord==mysteryWord:
      wintext,winBounds = showMessage("YOU WIN GG!!! Would you like to play again", 20, w/2, h/2,GREEN )
      surface.blit(wintext,winBounds)
   
      

#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:





# -------- Main Program Loop -----------
def main():
   gameInPlay = True
   numWrong = 0
   mysteryWord = getMysteryWord()
   userWord = "-"*len(mysteryWord)
   letterEntered = ""
   usedLetters = []
   print("Lets play Hangman!\n\n")
   print(userWord)
   #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    
   while (True):
        
      for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
               pygame.quit();                          #for ending the game & closing window
               sys.exit();
               
         if (event.type==pygame.KEYDOWN and gameInPlay):
            letterEntered =(event.unicode).lower()

            if(isValidLetter(letterEntered, usedLetters)):
               usedLetters.append(letterEntered)
               if letterEntered not in mysteryWord:
                  numWrong+=1
               userWord = updateUserWord(mysteryWord, usedLetters)
               # test game over-loss
               if numWrong == 6:
                  gameInPlay=False
               # test game over-win
               if mysteryWord==userWord:
                  gameInPlay=False
         if (event.type==pygame.KEYDOWN and gameInPlay==False and event.key==pygame.K_RETURN):
            gameInPlay = True
            numWrong = 0
            mysteryWord = getMysteryWord()
            userWord = "-"*len(mysteryWord)
            letterEntered = ""
            usedLetters = []               
              
           
           
           
      
      surface.fill(WHITE)                             #set background color
        
        #drawing code goes here
      drawScreen(userWord, numWrong, getMysteryWord,usedLetters)
     
      
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
      pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
