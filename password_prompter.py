# password = input("Enter your password: ")
#
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result["digit"] = digit
#
# uppercase = False
#
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result["uppercase"] = uppercase
#
# print(result)
#
# if all(result.values()):
#     print("Password accepted")
# else:
#     print("Password rejected")

ask = input("How many liters? ")

def lit_to_m3(ask):
    result = int(ask) / 1000
    return result
print(lit_to_m3(ask))