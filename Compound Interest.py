principal = float(input("What is your initial deposit?"))
rate = float(input("What is the annual interest rate (in decimal)?"))
num = float(input("How many times is interest ccompounded per year?"))
time = float(input("How many years is the money invested/borrowed for?"))
amount = principal * (((1+ (rate/num)) **(num * time)))
print(str(amount))
