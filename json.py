#                        converting JSON TO PYTHON
# import json

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

#                          CONVERTING PYTHON TO JSON

import json 

x = {
    "name":"john",
    "age" : 30 , 
    "city":"new york"
    }

y = json.dumps(x)
print(y)