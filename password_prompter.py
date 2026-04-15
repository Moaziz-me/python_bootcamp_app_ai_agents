

result = []
# while True:
password = input("Enter your password: ")
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)
digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

print(all(result))