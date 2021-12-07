months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'February', 'March', 'December']
monthss = (set(months))
print(len(monthss))
batch_sizes = [1,2,3,5, 700]
num1 = int(input("Enter A Number: "))
num2 = int(input("Enter Another Number: "))
num3 = int(input("Enter A Third Number: "))
print (max(num1, num2, num3 ))
print(min(num1, num2, num3))
print(sorted(months))
print(sorted(months, reverse= True))
print(max(batch_sizes))
month = months[6:9 + 1]
name = "Nifemi"
print(month)
print(len(months))
print("July" in months)
print("July" not in months)
print("Nifemi" in months)
print("Nifemi" not in months)
months[3] = "Nifemi"
print(months)
print("Nifemi" in months)
