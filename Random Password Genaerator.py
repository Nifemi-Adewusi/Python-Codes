import random
password = "ABCDEFHIJKLMNOPQRSTUVWXYXZ123456789();'[]=_=++?.,<>+==ABCSDETRJTTFGDbmieeeee"
password_length = int(input("Enter The Lenghth Of Your Password: "))
a = "".join(random.sample(password, password_length))
print(f"Your Password Is {a}")




