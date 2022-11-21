def tempConvert(c):
    return 9/5 * c + 32

def km_m(km):
    return km * 1000

temps = [34.4,27.6,20.9,33.6,37.8]
kms = [454,5.6,67,100]

f = list(map(tempConvert, temps))
print(f)

ms = list(map(km_m, kms))
print(ms)
