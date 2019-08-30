import random
from time import sleep

# Function For check if you enter string instead of integer
def inputNumber(num1):
  while True:
    try:
       userInput = int(input(num1))       
    except ValueError:
       print('\n',"Not an integer! Try again.",'\n')
       continue
    else:
       return userInput 
       break 

x = 1
yscore=0
mscore=0
escore=0

print('You Have Only 10 tries To won Good Luck....')
print('\n')

# 10 Tries Loop
while x <= 10:
    
    print('\n','Try Number: {} '.format(x))
    print('\n')
    y=inputNumber('Please Select Number From 1 To 10 : ')    
#check if you entered a number in range
    if y >10:
        print('\n',"Wrong Number. The number must be in the range of 1-10.")
        continue
    else:
        pass

        
        

#Let Pc Chose Rondom Number
    from random import *
    z = randint(0, 10) 
#Print Your Choice along with Pc Choice   
    print('\n','Your Choice Is: {}  |  Machine Choice Is: {}'.format(y,z))
    print('\n')
#Compare Choices and Count How Many times you won and how many times pc won also count Equivalence
    if y > z:
        print('You Won This Try Good Choice ....')
        print('\n')
        yscore+=1
    elif z>y:
        print('Machine Won This Try ....')
        print('\n')
        mscore+=1
    else:
        print('Equivalence')
        escore+=1
    x+=1

#Print Results
    
    if x>10:
        print('\n')
        wait = input("End Of Game PRESS ENTER TO Calculate Score......")
        sleep(3)
        print('\n')
        print('Your Score Is: {}  |  Machine Score Is: {}  |  Equivalence : {}'.format(yscore,mscore,escore))
        print('\n')
        if yscore>mscore:
            print('You Won Good Play ....')
            print('\n')
        
        elif yscore<mscore:
            print('Machine Won Good Luck Next Time ....')
            print('\n')
        
        else:
            print('Equivalence')
            print('\n')

#check If user wanna play again or no

        con = inputNumber('Wanna Try Again 1-yes 2-No :  ')
        if con == 1:
          x=1
          yscore=0
          mscore=0
          escore=0
          continue
        else:
          
          break
        

        
    else:
       continue
       
         
      
