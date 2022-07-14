''' Assignment 7
Anirudh Ralhan, bt21107091
'''

# Question 4

print("Question 4")

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  
        quicksort(pi+1, r, nums)  
    return nums

input_list = []
n = int(input("Enter number of elements in list : "))
for i in range(0,n):
    element = int(input("enter element : "))
    input_list.append(element)
    
print("Sorted list is : ",quicksort(0,len(input_list)-1,input_list))

print("----------------------------------------------")


