""" question 1 from the oxford finance interview """
""" solving number of unique completely fiilling paths in a 3x3 grid """

import numpy as np
import random


#define the boundaries of the shape to be traversed
banlist=[]

banlist.append([0,0])
banlist.append([1,0])
banlist.append([2,0])
banlist.append([3,0])
banlist.append([4,0])

banlist.append([4,1])
banlist.append([4,2])
banlist.append([4,3])

banlist.append([0,1])
banlist.append([0,2])
banlist.append([0,3])
banlist.append([4,4])

banlist.append([1,4])
banlist.append([2,4])
banlist.append([3,4])

import copy
shape_definition = copy.copy(banlist)

# 00 10 20 30 40
# 01          41
# 02          42
# 03          43
# 04 14 24 34 44
#

# print(banlist)

#now lets take a random walk around the bounded area, noting our steps



def move(xyold):
    """ moves randomly by 1 in either x or y """
    import copy
    xy = copy.copy(xyold)
    x_or_y =random.randint(0,1)
    plus_or_minus = random.randint(0,1)

    if x_or_y==0:
        if plus_or_minus==0:
            xy[0]=xy[0] +1
        if plus_or_minus==1:
            xy[0]=xy[0] -1

    if x_or_y==1:
        if plus_or_minus==0:
            xy[1]=xy[1] +1
        if plus_or_minus==1:
            xy[1]=xy[1] -1

    return xy


def stuck_check(xy,banlist):
    """ check if the walker has gotten stuck """

    if ([xy[0]+1,xy[1]] in banlist) == True:
        if ([xy[0]-1,xy[1]] in banlist) == True:
            if ([xy[0],xy[1]+1] in banlist) == True:
                if ([xy[0],xy[1]-1] in banlist) == True:
                    'walker is stuck, terminating'
                    return True

    return False


def find_path():

    banlist = copy.copy(shape_definition)
    walklist = []
    startpos  = [random.randint(1,3),random.randint(1,3)]

    position = startpos;print(startpos)
    walklist.append(startpos)
    banlist.append(startpos)
    i=0 # i is successfull moves
    while i!=9: #nine grid squares

        if stuck_check(position,banlist) == True:
            i = 9 # end the search and restart

        newposition = move(position);
        print(position,newposition)
        print(newposition in banlist)

        if (newposition in banlist) == False:
            #print('move success')
            i = i+1
            banlist.append(newposition)
            walklist.append(newposition)

            position = newposition

    print('walklist',walklist)

    return walklist

walklist=find_path()
if len(walklist)==9:
    print('path found')
if len(walklist)!=9:
    print('no path found')


goodpaths=[]
for j in np.arange(5000):

    walklist = find_path()
    if len(walklist)==9:
        print('path found')
        if (walklist in goodpaths) == False:
            print('path not a duplicate ')

            goodpaths.append(walklist)

print('number of paths found ',len(goodpaths))

### seems to be a limit of 40 paths


### now search for paths that are directional copies of each other

unique_paths = []
for k in goodpaths:
    if (k in unique_paths) == False:
        if (k[::-1] in unique_paths) == False:
            unique_paths.append(k)

print(len(unique_paths),'paths are non directionally reversed copies ')


""" This second answer is presumably the one asked for in the interview """
