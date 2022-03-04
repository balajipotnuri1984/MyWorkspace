# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    for i in range(-1000000,1000000):
        if i >= min(A) :
            if i in A:
                #print(i)
                continue
            else:
                if i <= 0:
                    return 1
                else:
                    #print(i)
                    return i
print('The smallest positive interger that does not occur in A', solution([1, 3, 6, 4, 1, 2]))
print('The smallest positive interger that does not occur in A', solution([1, 3, 5, 10, 1, 2]))

print('The smallest positive interger that does not occur in A', solution([-1,1]))

print('The smallest positive interger that does not occur in A', solution([1,1000]))
