'''
Given a number of socks with a number code corresponding to a color, how many pairs exist?

Sample Input:
10
1 1 3 1 2 1 3 3 3 3

'''

if __name__ == '__main__':
	n = int(input('Number of Socks: '))
	ar = [int(item) for item in input('List of Socks: ').split()]

	colors = set(ar)
	pairs = 0
	count = 0
	for i in colors:
	    if ar.count(i) != 1:
	        pairs = pairs + (ar.count(i)//2)
	print('Total Pairs:', pairs)
