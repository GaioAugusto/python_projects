#This program calculates how many dollars each person has to tip to the waiter of a restaurant.
#The program assumes each person will pay for their own meal and only split the service tax

# [PT-BR]
# Esse programa calcula quanto dinheiro cada pessoa tem que dar de gorjeta para um garçom em um restaurante.
# O programa supõe que cada pessoa pagará por sua própria refeição e vai dividir apenas a taxa de serviço

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give?"))
num_people = int(input("How many people are splitting this bill? "))

if num_people == 0:
    print("You cannot split the bill in zero people")
else:
    result = round((total_bill*tip_percentage/100)/num_people, 2)
    print(f"Each person should pay: {result}")
