inputF = float(input("What is the degrees in Fahrenhenheit?"))
celcius = (inputF - 32) * (5/9)
inputC = float(input("What is the degrees in Celcius?"))
fahr = (inputC * (9/5)) + 32
celciusRound = round(celcius, 2)
fahrRound = round(fahr, 2)
print(str(celciusRound) + " is your conversion from F to C and " + str(fahrRound) + " is your conversion from C to F")
               
