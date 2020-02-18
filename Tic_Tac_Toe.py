print("welcome to Tic_Tac_Toe")
l=[]
m=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def display():
    print("***************\n")
    print(m[0][0]," | ",m[0][1]," | ",m[0][2])
    print("________________")
    print(m[1][0]," | ",m[1][1]," | ",m[1][2])
    print("________________")
    print(m[2][0]," | ",m[2][1]," | ",m[2][2])
    print("\n***************")

def Get_Input(a):
    
    box=int(input("Enter the position '1' to '9'-->"))
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

def Round():
    i=0
    c=0
    while i<4:
       
        display()
        Get_Input('x')
        z=Winer_checking('x')
        if z==1:
            display()
            print(" x is winner")
            print("Game over")
            break
        c=c+1
        display()
        Get_Input('o')
        z=Winer_checking('o')
        if z==1:
            display()
            print("o is winner")
            print("game over")
            break

        display()
        if c==4:
            z=Get_Input('x')
            z=Winer_checking('x')
            if z==1:
                display()
                print("x is winner")
                print("game over")
            else:
                display()
                print("game tie")
                print("game over")
                
        i=i+1

def Winer_checking(plyer):
    i=0
    j=0

    while i<3:
        
        if   m[i][j]==plyer and m[i][j+1]==plyer and m[i][j+2]==plyer:
            
            return 1
        i=i+1

    i=0

    while j<3:
        if m[i][j]==plyer and m[i+1][j]==plyer and m[i+2][j]==plyer:
            
            return 1
        j=j+1

  
    i=0
    j=0
    if m[i][j]==plyer and m[i+1][j+1]==plyer and m[i+2][j+2]==plyer:
       
        return 1



    elif m[i][j+2]==plyer and m[i+1][j+1]==plyer and m[i+2][j]==plyer:
        
        return 1
        
        
Round()
