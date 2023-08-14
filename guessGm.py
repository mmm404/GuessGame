from random import randint

true_guess=randint(1, 10)

user_guess=input('Enter a numerical guess between 1-10')




while True:
  
  try:
   
    if true_guess==int(user_guess):
     
      print('Hurray! you are the genius ')

 
    else: 
     
      print('You lose, Do you wish to proceed with the game? (Y/N)')
 
  except ValueError as err:
    
    print('your guess should be numerical')
    



