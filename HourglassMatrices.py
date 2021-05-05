'''
Given a 2D n x n array, find the largest sum of values in an "hourglass" configuration.

Hourglass shape example
A B C
  D
E F G

Sample Input:
6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6

'''

n = int(input('Choose size of n x n matrix: n = '))
arr = []
sums = []

for i in range(n):
    line = [int(item) for item in input('Input your array, row %s of %s: ' % (i, n)).split()]
    arr.append(line)
    
for i in range(n-2):
    for j in range(n-2):
        if j > n-4:
            hourglass = sum(arr[i][j:]) + arr[i+1][j+1] + sum(arr[i+2][j:])
            sums.append(hourglass)
        else:
            hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            sums.append(hourglass)

print(max(sums))
