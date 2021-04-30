import sys
import random

sys.setrecursionlimit(1000000)

#############       FUNÇÕES       ##############################################################
def quick_sort(array, n):
    quicksort(array, 0, n-1)

def quicksort(array, inicio, fim):
    if (inicio < fim):
        pi = partition(array, inicio, fim)

        quicksort(array, inicio, pi - 1)
        quicksort(array, pi + 1, fim)


def partition(array, inicio, fim):
    pidx =  random.randrange(inicio, fim)
    pivo = array[pidx]
    array[fim], array[pidx] = array[pidx], array[fim]

    i = (inicio - 1)
    for j in range(inicio, fim):

        if (array[j] <= pivo):
            i += 1

            array[i], array[j] = array[j], array[i]
    array[i + 1], array[fim] = array[fim], array[i + 1]

    return (i + 1)

