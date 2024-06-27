# import re

# def validate_password(check_password):
#     password = check_password
#     if not(8 <= len(password) <= 20):
#         return "Your password is weak"
#     if not (re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'\d', password)):
#         return "Your password is weak"
#     if re.sub(r'[a-zA-Z0-9!.]', '', password):
#         return "Your password is weak"
#     if re.search(r'(.)\1', password):
#         return "Your password is weak"
#     return "Your password is strong"

# password = input('Enter your password: ')
# print(validate_password(password))

# # password= input('enter your password :- ')



# array1 = [[ "Apple", "Banana"],
# ['Apricot', 'Orange', 'Almonds', 'Guava'],
# ['Grapes', 'Strawberry', 'Lichie']
# ]

# array2 = [["Apple"],
# ["Banana", 'Orange', 'Apricot', 'Orange', 'Almonds', 'Guava'],
# ['Grapes', 'Strawberry','Lichie', 'Grapes', 'Grapes']]

# def find_common_elements(arr1, arr2):
#   set1 = set(array1)
#   set2 = set(array2)
  
array1 = [[ "Apple", "Banana"],
['Apricot', 'Orange', 'Almonds', 'Guava'],
['Grapes', 'Strawberry', 'Lichie']
]

array2 = [["Apple"],
["Banana", 'Orange', 'Apricot', 'Orange', 'Almonds', 'Guava'],
['Grapes', 'Strawberry','Lichie', 'Grapes', 'Grapes']]
 
result = []
for subarray1 in array1:
    temp = []
    for element in subarray1 :
        for i , subarray2 in enumerate(array2):
            if element in subarray2:
                temp.append((i,subarray2.index(element)))
    result.append(temp)   

print(result)        

