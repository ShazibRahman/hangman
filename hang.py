print('WELCOEME TO MY HANGMAN ')
#importing the library_hehehe
from colorama import Fore as f ,Style as s
import time
import random as rd 
from extra import display_hangman
def ext():
    print()
    for i in range(5):
        print(f'\rprogram will be ended in {f.RED}{5-i}{s.RESET_ALL} secs',end="")
        time.sleep(1)
    print(f'\rended:---                                                                ',end="\n\n\n")
    exit()


#asking user it's name and hether he wants to play or not
name=input(f"enter your name \n")

wanna_play=input(f"{name} do you wana continue enter y/yes or n/no \n")
if wanna_play.lower()=='n' or wanna_play.lower()=='no':
    print(f"{f.MAGENTA}{s.DIM}why did u do that???   ;-( {s.RESET_ALL} ")
    ext()#exitting the process in case usr dont want to play
print("thank_god u choose to play:\n")
choice_list=['choice','letter','table','avenger','hek','python','icecream','computer','kite','hyderabad','mobile',]

alphabet='a b c d e f g h i j k l m n o p q r s t u v w x y z'
alpha=alphabet.split()
#code for repetating the choosing word part
bool=True
while bool ==True:
 print(f'{f.YELLOW}guess the word Wish u a luck and three i.e. 5F wrong attempt and you are gone\n')
 print('enter only a lettet at a time a-z/1\n')
 gug=[]
 loss=True
 choosen_word=rd.choice(choice_list)#randomly choosing a word using random.choice function
 n=rd.randint(0,len(choosen_word)-1)
 m=rd.randint(0,len(choosen_word)-1)
 if n==m:#in case if both are equal then user might get only one pre guess
     m=(len(choosen_word)-1)
     n=0 # i gave n=0  because what if n's and m's value is equal to len-1 so that's why i  did that 
 #print(n,m)
 guess_word =['-' for x in range(len(choosen_word))]#creating a hangman list comoposed tof this '---' hehe

 guess_word[n]=choosen_word[n]#pre guessing two words for the player for a better guess
 guess_word[m]=choosen_word[m]
 print(guess_word)
 y=0
#actual hangman_part_repetative_guessing
 print("no of attempts you have: 6")
 print(display_hangman(6))
 while(y<6):

    
    
    guess=input("enter one input at a time:     ")
    
    
    
    if guess  in gug:
       print("Word is already guessed")
       print("no of attempt left: ",6-y)
       print(display_hangman(6-y))
       continue
    elif guess in '  ' or guess not in alpha:
       print("invalid move")
       
       if y<=6:
          print("no of attempt left: ",6-y)
          print(display_hangman(6-y))
       continue
       
    else:
       gug.append(guess)
   
       
       
       #processing the inputs 
       if guess.lower() in choosen_word:
            print(f'{guess} is matched gr8')
            
               
            
            for x in range(len(choosen_word)):#guessing_repetative_word
                if choosen_word[x]==guess:
                    guess_word[x]=guess
            
            print(guess_word)
            print(display_hangman(6-y))
            
            if "-" not in guess_word:
                print(f"{f.GREEN}\nwell played:{name} \
and  no.of wrong attempts:{s.BRIGHT} {y}{s.RESET_ALL}")
                loss=False
                
                break
            continue
       else:
            print(f"not matched no '{guess}' is in the letter  enter again")
            print(guess_word)
            y+=1
            if y<=6:
               print("no of attempt left: ",6-y)
              
               print(display_hangman(6-y))
             
            continue
   
            
#if try>2 game over
 if loss:
     
     print(f"\n{f.RED}better luck next time you are out of attempts and the word is : {s.BRIGHT}{choosen_word.upper()}{s.RESET_ALL}\n")#displaying the word in case user dont get this right
 x_re=input(f"\n{f.CYAN}do you want to play again : y/yes for yes if no press any key:{s.RESET_ALL} ")
 print()
 if x_re.lower()=='y' or x_re.lower()=="yes":
     
     continue
 #exit the code if the user dont want to continue 
 
 else:
     print(f'\n{s.DIM}{f.MAGENTA}sorry to see you go   ;-(  {s.RESET_ALL}\n' )#hehe i really don't felt that.
     ext()
     
