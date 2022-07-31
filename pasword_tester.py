import string

password = input("Enter your password: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open("common.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score: 0 / 8")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 15:
    score += 1
if length > 15:
    score += 1
if length > 20:
    score += 1
print (f"Password length is {str(length)}, adding {str(score)} Points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} Points!")

if score < 4:
    print(f"The password is quite weak! Score: {str(score)} / 8 ")
elif score == 4:
    print(f"The password is ok! Score: {str(score)} / 8")
elif score > 4 and score < 6:
    print(f"The password is pretty good! Score: {str(score)} / 8")
elif score > 6:
    print(f"The password is strong! Score: {str(score)} / 8")
