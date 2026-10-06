def reverse_list(arr):
    reversed_arr=[]
    for i in range(len(arr)-1,-1,-1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1,2,3,4,6]))
print(reverse_list(["A","B","C"]))
