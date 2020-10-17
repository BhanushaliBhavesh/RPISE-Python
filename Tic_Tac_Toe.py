print("welcome to Tic_Tac_Toe")
l=[]
m=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
#function for displyaing Tic_Tac_Toe box
def display():
    print("***************\n")
    print(m[0][0]," | ",m[0][1]," | ",m[0][2])
    print("________________")
    print(m[1][0]," | ",m[1][1]," | ",m[1][2])
    print("________________")
    print(m[2][0]," | ",m[2][1]," | ",m[2][2])
    print("\n***************")
    
#Function for intgercheck
def IntCheck(a):
    try:
        int(a)
        return 1
    except:
        return 0


#function for getting input from user
def Get_Input(a):
    z=input("Enter the postion 1 to 9 --->")
    c=IntCheck(z)
    if c==1:
        box=int(z)
        if box in l:
            print("this task is not valid")
            Get_Input(a)
        else:
            l.append(box)
            if box in range(1,10):
                if box==1:
                    m[0][0]=a
                elif box==2:
                    m[0][1]=a
                elif box==3:
                    m[0][2]=a
                elif box==4:
                    m[1][0]=a
                elif box==5:
                    m[1][1]=a
                elif box==6:
                    m[1][2]=a
                elif box==7:
                    m[2][0]=a
                elif box==8:
                    m[2][1]=a
                elif box==9:
                    m[2][2]=a
            else:
                print("Enter valid number")
                Get_Input(a)
    else:
        print("Enter valid number")
        Get_Input(a)
    
   

#function for managing users turn
def Round():
    i=0
    c=0
    while i<4:
       
        display()
        Get_Input('x')
        z=Winner_checking('x')
        if z==1:
            display()
            print(" x is winner")
            print("Game over")
            break
        c=c+1
        display()
        Get_Input('o')
        z=Winner_checking('o')
        if z==1:
            display()
            print("o is winner")
            print("game over")
            break

        display()
        if c==4:
            z=Get_Input('x')
            z=Winner_checking('x')
            if z==1:
                display()
                print("x is winner")
                print("game over")
            else:
                display()
                print("game tie")
                print("game over")
                
        i=i+1

#function for checking winner
def Winner_checking(player):
    i=0
    j=0

    while i<3:
        
        if   m[i][j]==player and m[i][j+1]==player and m[i][j+2]==player:
            
            return 1
        i=i+1

    i=0

    while j<3:
        if m[i][j]==player and m[i+1][j]==player and m[i+2][j]==player:
            
            return 1
        j=j+1

  
    i=0
    j=0
    if m[i][j]==player and m[i+1][j+1]==player and m[i+2][j+2]==player:
       
        return 1



    elif m[i][j+2]==player and m[i+1][j+1]==player and m[i+2][j]==player:
        
        return 1

Round()
