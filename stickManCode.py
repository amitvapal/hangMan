'''
Amitva Pal
Period 6/7 HCP
Unit 5 Loops
console version of hangman
'''




import random
def getMysteryWord():
    wordList = ["concatenation", "programming", "python", "function", "computer", "binary", "logic", "loop","statement"]
    return random.choice(wordList)


def isValidLetter(letter):
    


def main():
    gamaeInPlay = True
    numWrong = 0
    mysteryWord = getMysteryWord()
    userWord = "_ "*len(mysteryWord)
    usedLetters = []
    print("Lets play Hangman!\n\n")
    
    while(gameInPlay):
        print("Current Word: ", userWord)
        print("You have", 6-numWrong,"incorrect guesses left lol.")
        
        
        letter = input("Guess the letter: ").lower()
        #make suere letter is valid
        if(isValidLetter(letter, usedLetters)):
            usedLetters.append(letter)
            if letter not in mysteryWord:
                numWrong+=1
            userWord = updateUserWord(userWord, mysteryWord, usedLetters)
            
            
            
            #return false for all invalid enteries
            if len(letter)!=1:
                print("Invalid letter entered")
                return False
            if letter>"z" or letter<"a":
                print("Invalid letter entered")
                return False
            if letter in usedLetters:
                print("You have alread choosen this letter")
                return False
            return True
    
    





main()