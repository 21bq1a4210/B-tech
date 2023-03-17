import random
n = random.randint(1,6)
u=input('EVEN or ODD:')
u1=u.lower()
chance=int(input('enter any number in between 1 to 6:'))
print('computer choose:',n)
add=n+chance
your_runs=0
comp_runs=0
choose_bat_ball=''
c=random.randint(1,2)
if add%2==0:
    print(add,'is even')
else:
    print(add,'is odd')
if (add%2==0 and u1=='even')or(add%2!=0 and u1=='odd'):
    choose_bat_ball=input('BAT or BALL:')
    if choose_bat_ball=='bat':
                print('___________________________________________\n You choose bat first\n')
                while 1:
                    bat=int(input('enter your batting runs:'))
                    comp_bowl=random.randint(1,6)
                    if bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                        print('computer choose:',comp_bowl)
                    if bat==comp_bowl:
                        print ("Computer Guess: ",comp_bowl)
                        print ("You are Out. Your Total Runs= ", your_runs,"\n")
                        break
                    elif bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                    else:
                        your_runs= your_runs+bat
                        print ("Computer Guess: ",comp_bowl)
                        print ("Your total runs: ",your_runs,"\n")
                        
    elif choose_bat_ball=='ball':
                print('___________________________________________\n You choose ball first\n')
                while 1:
                    bat=int(input('enter your oppenent batting runs:'))
                    comp_bowl=random.randint(1,6)
                    if bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                        print('computer choose:',comp_bowl)
                    if bat==comp_bowl:
                        print ("Computer Guess: ",comp_bowl)
                        print ("computer was Out. computer Total Runs= ", comp_runs,"\n")
                        break
                    elif bat>6:
                        print ("ALERT!! Support No only till 6\n")
                        continue
                    else:
                        comp_runs=comp_runs+comp_bowl
                        print ("Computer Guess: ",comp_bowl)
                        print ("computer total runs: ",comp_runs,"\n")
                        
else:
  
    if c==1:
        
        print('___________________________________________\n Computer choose bat first\n')
        while 1:
            bat=int(input('enter your oppenent batting runs:'))
            comp_bowl=random.randint(1,6)
            if bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
                print('computer choose:',comp_bowl)
            if bat==comp_bowl:
                print ("Computer Guess: ",comp_bowl)
                print ("computer was Out. Computer Total Runs= ", comp_runs,"\n")
                break
            elif bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
            else:
                comp_runs= comp_runs+comp_bowl
                print ("Computer Guess: ",comp_bowl)
                print ("computer total runs: ",comp_runs,'\n')
                
                
                
    elif c==2:
        
        print('___________________________________________\n Computer choose ball first\n')
        while 1:
            bat=int(input('enter your batting runs:'))
            comp_bowl=random.randint(1,6)
            if bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
                print('computer choose:',comp_bowl)
            if bat==comp_bowl:
                print ("Computer Guess: ",comp_bowl)
                print ("you are Out. your Total Runs= ", your_runs,"\n")
                break
            elif bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
            else:
                your_runs= your_runs+bat
                print ("Computer Guess: ",comp_bowl)
                print ("Your total runs: ",your_runs,"\n")
                
#######################################################################################                
            
if choose_bat_ball=='bat':
    print('___________________________________________\n Computer started bating\n')
    while 1:
                    bat=int(input('enter your oppenent batting runs:'))
                    comp_bowl=random.randint(1,6)
                    if bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                        print('computer choose:',comp_bowl)
                    if bat==comp_bowl:
                        print ("Computer Guess: ",comp_bowl)
                        print ("computer was Out. computer Total Runs= ", comp_runs,"\n")
                        break
                    elif bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                    else:
                        comp_runs=comp_runs+comp_bowl
                        print ("Computer Guess: ",comp_bowl)
                        print ("computer total runs: ",comp_runs,"\n")
                        c=10
                                            
elif choose_bat_ball=='ball':
    print('___________________________________________\n You started bating\n')
    while 1:
                    bat=int(input('enter your batting runs:'))
                    comp_bowl=random.randint(1,6)
                    if bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                        print('computer choose:',comp_bowl)
                    if bat==comp_bowl:
                        print ("Computer Guess: ",comp_bowl)
                        print ("You are Out. Your Total Runs= ", your_runs,"\n")
                        break
                    elif bat>6 :
                        print ("ALERT!! Support No only till 6\n")
                        continue
                    else:
                        your_runs= your_runs+bat
                        print ("Computer Guess: ",comp_bowl)
                        print ("Your total runs: ",your_runs,"\n")
                        c=10
                        
if c==1:
    print('___________________________________________\n You sarted batting\n')
    while 1:
            bat=int(input('enter your batting runs:'))
            comp_bowl=random.randint(1,6)
            if bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
                print('computer choose:',comp_bowl)
            if bat==comp_bowl:
                print ("Computer Guess: ",comp_bowl)
                print ("you are Out. your Total Runs= ", your_runs,"\n")
                break
            elif bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
            else:
                your_runs= your_runs+bat
                print ("Computer Guess: ",comp_bowl)
                print ("Your total runs: ",your_runs,"\n")
                c=10
                            
elif c==2:
        print('___________________________________________\n Computer started bating\n')
        while 1:
            bat=int(input('enter your oppenent batting runs:'))
            comp_bowl=random.randint(1,6)
            if bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
                print('computer choose:',comp_bowl)
            if bat==comp_bowl:
                print ("Computer Guess: ",comp_bowl)
                print ("Computer is Out. Computer Total Runs= ", comp_runs,"\n")
                break
            elif bat>6 :
                print ("ALERT!! Support No only till 6\n")
                continue
            else:
                comp_runs= comp_runs+comp_bowl
                print ("Computer Guess: ",comp_bowl)
                print ("Your total runs: ",comp_runs,"\n")
                c=10
if comp_runs>your_runs:
    print('Your runs is',your_runs,'.Computer runs is',comp_runs)
    print('you loss')
    quit()
else:
    print('Your runs is',your_runs,'.Computer runs is',comp_runs)
    print('you won')
    quit()