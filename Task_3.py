def solution(S):

    a_count=1
    b_count=1
    ab_count=1
    ba_count=1
    i_cnt=1

    MinPosLen_a=[]
    MinPosLen_b=[]
    MinPosLen_ab=[]
    MinPosLen_ba=[]

    Temp = S.replace('?', 'a')
    for i in Temp:
        for j in Temp[i_cnt:]:
            if(i==j):
                a_count= a_count+1
                continue
            else:
                break
        MinPosLen_a.append(a_count)
        i_cnt=i_cnt+1
    i_cnt=1
    Temp = S.replace('?', 'b')
    for i in Temp:
        for j in Temp[i_cnt:]:
            if(i==j):
                b_count= b_count+1
                continue
            else:
                break
        MinPosLen_b.append(b_count)


    i_cnt=1
    Temp = S.replace('??', 'ab')
    for i in Temp:
        for j in Temp[i_cnt:]:
            if(i==j):
                ab_count= ab_count+1
                continue
            else:
                break
        MinPosLen_ab.append(ab_count)


    i_cnt=1
    Temp = S.replace('??', 'ba')
    for i in Temp:
        for j in Temp[i_cnt:]:
            if(i==j):
                ba_count= ba_count+1
                continue
            else:
                break
        MinPosLen_ba.append(ba_count)


    print(MinPosLen_a)
    print(MinPosLen_b)
    print(MinPosLen_ab)
    print(MinPosLen_ba)
    if(S.find('??')):
        return (min(MinPosLen_a[0], MinPosLen_ab[0]))
    else:
        return(min(MinPosLen_a[0],MinPosLen_b[0],MinPosLen_ab[0],MinPosLen_ba[0]))

print('The Solution is',solution("aa??bbb"))
print('The Solution is',solution("a?b?aa?b?a"))
print('The Solution is',solution("??b??"))
print('The Solution is',solution("aa?b?aa"))

