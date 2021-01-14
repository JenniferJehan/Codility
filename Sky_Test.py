# msg_t ='b'
# for x in range(1,15000):
#     msg_t += 'a'
# for x in range(1,15000):
#     msg_t += 'b'

def solution1(msg):
    temp = [[],[]]
    switch = True
    for x in msg:
        if x == 'b':
            switch = False
        if switch == True:
            temp[0].append(x)
        if switch == False:
            temp[1].append(x)
    if 'a' in temp[1] or 'b' in temp[0]:
        return False
    else:
        return True

# print(solution1(msg_t))

A = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def solution2(A):
    type1 = []
    type2 = []
    c1 = 0
    c2 = 0
    for x in range(0,len(A)):
        if x%2 == 1:
            type1.append(0)
            type2.append(1)
        else:
            type1.append(1)
            type2.append(0)
        if A[x] != type1[x]:
            c1 += 1
        if A[x] != type2[x]:
            c2 += 1
    
    if c1 < c2:
        return c1
    else:
        return c2

# print(solution2(A))
S = 'aaaa'
C = [3,4,5,6]

def solution3(S,C):
    s = list(S)

    ind1 = 0
    ind2 = 0
    group_char = []
    group_price = []
    if len(set(s)) == 1:
        group_char.append(S)
        group_price.append(C)
    else:
        while ind1 < len(s)-1:

            ind2 = ind1

            while ind2 < len(s)-1:

                if s[ind1] != s[ind2+1]:
                    group_char.append(s[ind1:ind2+1])
                    group_price.append(C[ind1:ind2+1])
                    ind1 = ind2
                    break

                if ind2 + 1 == len(s)-1:
                    group_char.append(s[ind1:ind2+2])
                    group_price.append(C[ind1:ind2+2])

                ind2 += 1

            ind1 += 1

    print(group_char,group_price)
    

    final_cost = 0
    for x in range(0,len(group_char)):
        
        if len(group_price[x]) > 1:
            group_price[x].sort()
            for z in group_price[x][0:-1]:
                final_cost += z


    return final_cost

S = 'id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11'
def solution4(S):
    # write your code in Python 3.6
    y = S.split('\n')
    group = []
    for x in y:
        group.append(x.split(','))
    
    for x in group:
        if any(z == 'NULL' for z in x):
            group.remove(x)
    
    temp = []
    for n in group:
        l2s = ","
        temp.append(l2s.join(n))

    answer = ''
    l2s2 = "\n"
    answer = (l2s2.join(temp))
    
    return answer

    
# print(solution4(S))
A = [2]
B = [5,6]

def solution5(A,B):
    numbers = {1,2,3,4,5,6}
    flip = {1:6,2:5,3:4,4:3,5:2,6:1}

    check = True
    count = 0 
    
    while check == True:
        A.sort()
        B.sort()
        diff = abs(sum(A) - sum(B))

        if sum(A) > sum(B):
            #change biggest number in A to value closest to the difference between A and B
            #or change smallest number in B
            
            b1 = B[0]
            b2 = flip.get(B[0])
            a1 = A[-1]
            a2 = flip.get(A[-1])

            possB = numbers.copy()
            possA = numbers.copy()

            possB.remove(b1)
            possB.remove(b2)

            possA.remove(a1)
            possA.remove(a2)

            if A[-1] - diff in possA:
                A[-1] = A[-1] - diff
            elif B[0] + diff in possB:
                B[0] = B[0] + diff
            elif A[-1] - min(possA) >= max(possB) - B[0]:
                A[-1] = min(possA)
            elif max(possB) - B[0] > A[-1] - min(possA):
                B[0] = max(possB)

            count += 1

        if sum(A) < sum(B):
            # flip biggest num in b
            
            b1 = B[-1]
            b2 = flip.get(B[-1])
            a1 = A[0]
            a2 = flip.get(A[0])

            possB = numbers.copy()
            possA = numbers.copy()

            possB.remove(b1)
            possB.remove(b2)

            possA.remove(a1)
            possA.remove(a2)

            if B[-1] - diff in possB:
                B[-1] = B[-1] - diff
            elif A[0] + diff in possA:
                A[0] = A[0] + diff
            elif B[-1] - min(possB) >= max(possA) - A[0]:
                B[-1] = min(possB)
            elif max(possA) - A[0] > B[-1] - min(possB):
                A[0] = max(possA)

            count += 1
        
        else:
            check = False

        print(A,B)
            
    return count , A , B

print(solution5(A,B))