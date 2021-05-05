'''
A hike has some number of steps and a tracked path of ascents or descents. Each hike starts and ends at sea level.

Sample Input:
20
UUDDDDUDUUUDUUUUDDDD

'''

if __name__ == '__main__':
    steps = range(int(input()))
    path = [1 if item =='U' else -1 for item in list(input())]      #  convert ascent and descent to numerical values
    x = 0                                                           #  elevation
    valley=0
    for i in steps:
        x+=path[i]
        if x <0 and x + path[i+1] == 0:                             #  One valley for each elevation drop below sea level and rises back to sea level
            valley+=1
    print(valley)
