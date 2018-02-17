L=[1,2,3,4,5,6,7,8,9,10]
count=0
counter=0

p1=int(input("Player 1, enter number from 1 to 10: "))    
while p1 not in L:    
    p1=int(input("make sure the number is in range from 1 to 10: "))
count=count+p1
print ("sum=",count)
           

while True:    

    if counter%2==0:           
        p2=int(input("Player 2, enter number from 1 to 10: "))
        while p2 not in L or p2 == p1:
          p2=int(input("Try another number: "))
        count=count+p2
        print("sum=",count)
        if count==100:
            break

    if counter%2!=0:     #player 1
        p1=int(input("Player 1, enter number from 1 to 10: "))
        while p1 not in L or p1 == p2:
          p1=int(input("Try another number: "))
        count=count+p1
        print ("sum=",count)
        if count==100:
            break        

    counter=counter+1
    
if counter%2==0:
    print ("player 2 won")
else:
    print ("player 1 won")
