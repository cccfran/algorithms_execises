# Using Moore's Voting Algorithm

def majority(arr):
    count = 0
    majority = arr[0]
    for i in arr:
        if i == majority:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            majority = i
            count = 1

    if arr.count(majority) > len(arr)/2:
        return majority
    else:
        return None


if __name__ == '__main__':
    arr = [1,2,2,2,2,3,4]
    print arr
    print len(arr)
    maj = majority(arr)

    if maj:
        print maj
    else:
        print "majority element does not exist"
