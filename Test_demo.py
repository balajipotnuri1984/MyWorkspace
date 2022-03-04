###Task 1 - Fuel dispenser(3 Tanks with different capacity) for Cars(5)

Wait_Timer = [0, 0, 2, 2, 8]
WaitTime =0
def solution(A,X,Y,Z):
    i=0
    while(i<len(A)):
        demand=A[i]
        if demand<=X and X>Z:
            X=X-demand
        elif demand<=Y and Y>Z:
            Y=Y-demand
        elif demand<=Z:
            Z=Z-demand
        else:
            if demand>max(X,Y,Z):
                print(demand,max(X,Y,Z))
                return -1
            else:
                i=i-1
                print('demand is',demand)
        if(demand==0):
            break
        else:
            WaitTime = Wait_Timer[i]
            print('the Dispenser remaining is ',X,Y,Z)
            i=i+1
    return WaitTime
print('The solution is ',solution([3,5,2,3,0],6,8,1))
print('The solution is ',solution([2,8,4,3,2],7,11,3))
print('The solution is ',solution([2,4,3,5,7],11,7,3))


###Task2 - Find the list of integers which are product of two consecutive numbers
def solution(list_a):
    IntCount=0
    for int_a in range(list_a[0],list_a[1]+1):
        #print(list_a[1])
        for i in range(1,list_a[1]+1):
            if(int_a == i*(i+1)):
                #print(int_a)
                IntCount= IntCount+1
            else:
                continue
    return IntCount
print('The Number of Intergers found ',solution([6,20]))
print('The Number of Intergers found ',solution([21,29]))