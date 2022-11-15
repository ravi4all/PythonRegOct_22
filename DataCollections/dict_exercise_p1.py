data = {
    "names" : ["John","Max","Nick","Shawn"],
    "dept" : ["IT","IT","HR","IT"],
    "salary" : [45000,80000,55000,25000]
    }

'''
for item in data:
    print(data[item])
'''

'''
for i in range(len(data["names"])):
    print(data["names"][i], data["dept"][i], data["salary"][i])
'''

#1. Fetch data of IT department only
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        print(data["names"][i], data["dept"][i], data["salary"][i])
    
#2. Sum of salary of IT dept
sum = 0
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        sum += data["salary"][i]

print("Total salary of IT :",sum)

#3. Take Emp Name as Input and print his details without using loop







