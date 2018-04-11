#!/bin/python3

import os
import sys

def getNeighbours(position, dimensions):
    neighbours = []
    for dim in range(len(dimensions)):
        if (position[dim] + 1) <= dimensions[dim]:
            neighbour = position[:]
            neighbour[dim] = neighbour[dim] + 1
            neighbours.append(neighbour)
        if position[dim] - 1 > 0:
            neighbour = position[:]
            neighbour[dim] = neighbour[dim] - 1
            neighbours.append(neighbour)
    return neighbours 

def scout(position, dimension_sizes, steps_left):
    if steps_left == 0:
        return 1
    else:
        possibilities = 0
        for neighbour in getNeighbours(position, dimension_sizes):
            possibilities += scout(neighbour, dimension_sizes, steps_left - 1)
        return possibilities

#
#
# Complete the gridWalking function below.
#
def gridWalking(m, x, D):
    return scout(x, D, m)%1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        x = list(map(int, input().rstrip().split()))

        D = list(map(int, input().rstrip().split()))

        result = gridWalking(m, x, D)

        fptr.write(str(result) + '\n')

    fptr.close()