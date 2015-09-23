import numpy as np

def find_int(array, start, count):
    if count == 0:
        return 0
    
    mid = start + (int)(count/2)

    print start, count, mid, array[mid]

    if array[mid] == mid:
        print mid
        return mid

#    if (array[mid] < start and array[mid] > start + count):
#       return 0

    num_left = (int)(np.ceil((count - 1)/2.0))
    print "num_left is ", num_left
    num_right = (int)((count-1)/2.0)

    if array[mid] > mid:
        return find_int(array, start, num_left)

    if array[mid] < mid:
        return find_int(array, mid+1, num_right)


if __name__ == '__main__':
    array = [0,-1,1,2,4,6,7,8,11,12,13]
    r = find_int(array, 1, len(array)-1)
    print r
