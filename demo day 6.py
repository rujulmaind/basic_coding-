# def f(i, values = []):
#     values.append(i)
#     print(values)

# f(1)
# f(2)
# f(3)

# def func(value, values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t, v[0])

# d = {'c': 97, 'a': 96, 'b': 98}

# for _ in sorted(d):
#     print(d[_])

# fruit ={}
# def addon(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addon('apple')
# addon('banana')
# addon('apple')
# print(len(fruit))


# Product of Array Except Self
# def productExceptSelf(nums):
#     n = len(nums)
#     output = [1] * n
#     prefix = 1
#     for i in range(n):
#         output[i] = prefix
#         prefix *= nums[i]
#     suffix = 1
#     for i in range(n - 1, -1, -1):
#         output[i] *= suffix
#         suffix *= nums[i]

#     return output
# nums = [1, 2, 3, 4]
# result = productExceptSelf(nums)
# print(result)

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0

# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)

#find second largest element
# list1 = [3, 1, 4, 1, 5, 9]
# list1.sort()
# print(list1)
# print(list1[-2])

#remove duplicates from unsorted array
# def remove_duplicates(arr):
#     seen = set()
#     result = []
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result
# arr = [1, 2, 3, 2, 4, 1, 5]
# print(arr)
# print(remove_duplicates(arr))

myset={1,2,"sanjay",5.66,"rahul","ayush","ramesh","ankit","rishikesh"}
print(myset)

# myset={1,2,"sanjay",5.66,"sanjay","rahul","ayush","ramesh","ankit","rishikesh"}
# print(myset)
# # print(myset[0])
# myset.add(60)
# print(myset)

# myset.discard(1)
# print(myset)    

myset.remove(2)
print(myset)    
