def majority(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]

    half = len(arr)/2

    maj_left = majority(arr[:half])
    print "left arr is ", arr[:half], " and the maj left is ", maj_left

    maj_right = majority(arr[half:])
    print "right arr is ", arr[half:], " and maj right is ", maj_right

    if (maj_left == maj_right):
        return maj_left

    if arr.count(maj_left) > len(arr)/2:
        return maj_left
    elif arr.count(maj_right) > len(arr)/2:
        return maj_right
    else:
        return None

if __name__ == '__main__':
    arr = [1,2,3,3,3,3,5]
    print arr
    print len(arr)
    maj = majority(arr)
    print
    print maj

