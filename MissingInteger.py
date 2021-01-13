"""Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""

A = [1, 3, 6, 4, 1, 2]
def solution(A):
    pos = [num for num in A if num >= 0]
    if len(pos) == 0:
        return 1
    elif len(pos) == 1:
        P = sorted(pos)
        count = 1
        Q = set(P)
        list = []
        for x in Q:
            if (x == count) and (isinstance(count, int) == True):
                list.append(count)
                count += 1
        return count
    else:
        P = sorted(pos)
        count = 1
        Q = set(P)
        list = []
        for x in Q:
            if (x == count) and (isinstance(count, int) == True):
                list.append(count)
                count += 1
        return count

print(solution(A))