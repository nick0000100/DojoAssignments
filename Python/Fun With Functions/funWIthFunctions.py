def odd_even():
    for count in range(1, 2000):
        if (count % 2 == 0):
            print "Number is " + str(count) + ". This is an even number."
        else:
            print "Number is " + str(count) + ". This is an odd number."

# odd_even()

def multiply(arr, val):
    for num in range(len(arr)):
        arr[num] *= val
    return arr


# a = [2,4,10,16]
# b = multiply(a, 5)
# print b
#[10,20,50,80]

def layered_multiples(arr):
    new_array = []
    for num in range(len(arr)):
        inner_arr = []
        for ones in range(0,arr[num]):
            inner_arr.append(1)
        new_array.append(inner_arr)
    return new_array

# x = layered_multiples(multiply([2,4,5],3))
# print x
