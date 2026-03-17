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
def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)

