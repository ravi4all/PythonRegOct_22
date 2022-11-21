def tempConvert(c):
    return 9/5 * c + 32

def km_m(km):
    return km * 1000

# c = 33.5
# f = tempConvert(c)
# print("Temperature is",f)

temps = [34.4,27.6,20.9,33.6,37.8]
f = []
for t in temps:
    f.append(tempConvert(t))

print(f)

kms = [454,5.6,67,100]
ms = []
for km in kms:
    ms.append(km_m(km))

print(ms)

