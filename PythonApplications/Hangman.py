
def hangman(x):
     if x==0:
         print(' ____\n|  |\n|\n|\n|\n|\n|')
     elif x==1:
         print(' ____\n|  |\n|  Q\n|\n|\n|\n|')
     elif x==2:
         print(' ____\n|  |\n|  Q\n|  |\n|  |\n|\n|')
     elif x==3:
         print(' ____\n|  |\n|  Q\n| \|\n|  |\n|\n|')
     elif x==4:
         print(' ____\n|  |\n|  Q\n| \|/\n|  |\n|\n|')
     elif x==5:
         print(' ____\n|  |\n|  Q\n| \|/\n|  |\n| /\n|')
     elif x==6:
         print(' ____\n|  |\n|  Q\n| \|/\n|  |\n| / \\\n|')



import os
import random as rn
#abc='αβγδεζηθικλμνξοπρστυφχψω'
abc='abcdefghijklmnopkrstuvwxyz'
with open('cities.txt','r') as w:
    wordtext=w.readlines()
    

lista=[]
for x in wordtext:
    x=x.replace('\n','')                 
    a,b=x.split(',')
    lista.append(a)
    lista.append(b)
 
while True:
    print('The Game starts\n')
    word=rn.choice(lista)
    word=word.lower()
    
    if word[0]==' ':word=word[1:]
    num_of_letters=len(word)
    printed_word=['_' for i in range (num_of_letters)]
    print('the word consists of',num_of_letters,'letters\n')
    wrong=0
    choices=[]
    
    while wrong<6 :
        c=input('Choose a letter: ')
        
        while c in choices:
            c=input('You have already chosen it, choose again: ')
        if c in word:
            choices.append(c)
            for i in range(num_of_letters):
                if c==word[i]:
                    printed_word[i]=c
                print(printed_word[i],end='',sep='')
            print('  Chosen letters:',choices)
        else:
            wrong+=1
            choices.append(c)
            for i in range(num_of_letters):
                print(printed_word[i],end='',sep='')
            if wrong==6:
                print(' Unfortunately you lost. The hidden word was:',word,'\n\n')
                hangman(wrong)
                continue
            print('  Wrong choice,another',6-wrong,'tries,   Chosen letters:',choices)
        
        hangman(wrong)

        print('\n\n')
        if '_' in printed_word:
            continue
        else:
            print('Congratulations \n\n')
            break
    
    del printed_word
    qu=input('\nPress "q" to stop   or   any other button to continue\n\n')
    if qu=='q':
        break


