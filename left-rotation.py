'''
Given an array of x integers, construct an operator which rotates elements by d positions to the left.

Sample Input:
6 7
1 2 3 4 5 6

Print as a string for some reason
'''

ad = [int(item) for item in input().split(" ")]
array = [int(item) for item in input().split(" ")]
new = [0]*ad[0]
st = ''
for i in range(ad[0]):
        if i < ad[1]:
            new[-(ad[1]-i)] = array[i]
        else:
            new[i-ad[1]]=array[i]

st = [str(item) for item in new]
final = ' '.join(st)
print(final)
