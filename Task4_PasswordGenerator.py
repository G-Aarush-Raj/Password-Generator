import random
import string

def generate_password(length):
    #Generate a random password with the length specified by user
    password=""
    characters= string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += ''.join(random.choice(characters))
    return password

print("Welcome to the Password Generator")
print("This tool will generate strong and secure passwords")
print()
while True:
    try:
        #Can generate n number of passwords
        num_passwords =int(input("Enter the number of passwords to generate: "))
        if num_passwords<=0:
            raise ValueError("Enter a positive integer")
        break
    except ValueError as e:
        print(e)
while True:
    try:
        length =int(input("Enter the length of each password: "))
        if length<=0:
            raise ValueError("Enter a positive integer")
        break
    except ValueError as e:
        print(e)
if length <=5:
    print("\nGenerating Easy Passwords:")
elif length <=9:
    print("\nGenerating Moderate Passwords:")
else:
    print("\nGenerating Hard Passwords:")
for _ in range(num_passwords):
    password = generate_password(length)
    print(password)
print("\nPasswords generated successfully!")