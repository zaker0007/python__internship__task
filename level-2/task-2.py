import random

password=[]
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
for i in range(5):  # Generate 5 random characters
    password.append(random.choice(letters))
    password.append(random.choice(numbers))

print("Generated password:", "".join(password))