import random
u = int(input("Enter length of password :"))

s = ("qwertyuioplkjhgfdsazxcvbnm")
def big():
    return s.upper()

n = "1234567890"
def nu():
    return n

c = "!@#$%^&*"
def sp():
    return c

# characte pool
character_pool = s + big() + nu() + sp()

password = ""

for i in range(u):
    password += random.choice(character_pool)

print("Generated Password:", password)
