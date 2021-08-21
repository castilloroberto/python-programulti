



def reverse( a ):
    
    reverse = []

    print(len(a)-1)
    
    for x in range(len(a)-1,-1,-1):
        print('x: ',x)
        reverse.append(a[x])

    return reverse



reversedArray = reverse([1,2,3,4,5,6])


print('reversedArray: ',reversedArray)

