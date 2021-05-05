'''
A hike has some number of steps and a tracked path of ascents or descents. Each hike starts and ends at sea level. This program counts the number of valleys and mountains.

                   /\
                  /  \
     /\          /    \
____/  \      /\/      \_____
        \    /
         \/\/


Sample Input:
20
UUDDDDUDUUUDUUUUDDDD

'''

if __name__ == '__main__':
    steps = range(int(input('Number of Steps: ')))
    path = [1 if item == 'U' else -1 for item in list(input('Elevation Path: '))]           #  convert ascent and descent to numerical values
    x = 0                                                
    valley = 0
    mountain = 0
    for i in steps:
        x += path[i]                                #  elevation tracker 
        if x < 0 and x + path[i+1] == 0:            #  One valley for elevation drop below sea level and rises back to sea level, vise versa for mtns
            valley += 1
        elif x > 0 and x + path[i+1] == 0:
        	mountain += 1
    print('Number of Valleys:', valley)
    print('Number of Mountains:', mountain)
