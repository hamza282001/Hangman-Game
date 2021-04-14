import random
import func1
import func2
file=open('words.txt','r')
rt=file.read()
ws=(rt.split())
file.close()

guess=[]
my_word=random.choice(ws)

length=len(my_word)
alphabet='abcdefghijklmnopqrstuvwxyz'
alp=list(alphabet)
consonant='bcdfghjklmnpqrstvwxyz'
vowel='aeiou'
used=[]

func1.letsbegin()


for i in my_word:
        guess.append("_")
print("I'm thinking of a word that is",length,"letters long.")
print("You have 6 GUESSES and 3 WARNINGS left. \nEnter only one alphabet at a time.")
print("-"*77)



func2.startguessing(my_word,used,length,guess,consonant,vowel)    

print("="*77)
print(" \t \t \t \t GAME OVER!")
print("="*77)

  
