age = input("Input how old you are in years")
age = int(age)
leftOver = age % 4
leftOver = int(leftOver)
days = age * 365.24 + leftOver
days = int(days)
print(days)
