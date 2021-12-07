prime = int(input("Enter A Number: "))
def check_prime(num):
    if num <= 1:
     return False
    for i in range(2, num):
        if num % i == 0:
         return False
        return True
    if check_prime(prime):
        print("The Number Is Prime")
    else:
        print("The Number Is Not Prime")

