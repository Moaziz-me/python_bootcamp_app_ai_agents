date = input("What date do you want?")
mood = input("What mood do you want?")
thoughts = input("What thought do you want?")

with open(f"{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thoughts + "\n")