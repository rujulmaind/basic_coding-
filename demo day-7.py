
# #print an integer representing the number of special characters and whilespaces present in a given message
# def count_special_characters(message):
#     count = 0
#     for char in message:
#         if not char.isalnum():  # Check if the character is not alphanumeric
#             count += 1
#     return count

# # Example usage
# message = "gasgg54@#vscdls"   
# result = count_special_characters(message)
# print("Number of special characters and whitespaces:", result)


# print an integer representing the number of special characters and whilespaces present in a given message seperately for each
# def count_special_characters_and_whitespace(message):
#     special_char_count = 0
#     whitespace_count = 0
    
#     for char in message:
#         if char.isspace():  # Check if the character is a whitespace
#             whitespace_count += 1
#         elif not char.isalnum():  # Check if the character is not alphanumeric
#             special_char_count += 1
            
#     return special_char_count, whitespace_count

# # Example usage
# message = "gasgg54@#vscdls  "  
# special_char_count, whitespace_count = count_special_characters_and_whitespace(message)
# print("Number of special characters:", special_char_count)
# print("Number of whitespaces:", whitespace_count)

#find the intersection of three arrays using one loop
# def find_intersection(arr1, arr2, arr3):
#     intersection = []
#     for num in arr1:
#         if num in arr2 and num in arr3:
#             intersection.append(num)
#     return intersection
# # Example usage
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 4, 5, 6, 7]
# arr3 = [5, 6, 7, 8, 9]
# result = find_intersection(arr1, arr2, arr3)
# print("Intersection of the three arrays:", result)

# given an array, move all the zeroes to the end without changing the order of non-zero elements
# def move_zeroes_to_end(arr):
#     non_zero_index = 0
    
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_index] = arr[i]
#             non_zero_index += 1
            
#     for i in range(non_zero_index, len(arr)):
#         arr[i] = 0
        
#     return arr
# # Example usage
# arr = [0, 1, 0, 3, 12]
# result = move_zeroes_to_end(arr)
# print("Array after moving zeroes to the end:", result)


# find the second largest number in an array
def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find the second largest
    
    first_largest = second_largest = float('-inf')
    
    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None
# Example usage
arr = [3, 1, 4, 1, 5, 9]
result = find_second_largest(arr)
print("The second largest number in the array is:", result)


    