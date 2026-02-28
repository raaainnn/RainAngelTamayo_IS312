#MULTIPLY 2 NUMBERS INPUT BY THE USER

print("Good day! We are going to multiply 2 numbers.")
print("_____________________________________________")

tamayoRain_ans = "y"
while tamayoRain_ans == "y":

    tamayoRain_num1 = int(input("Enter first number: "))
    tamayoRain_num2 = int(input("Enter second number: "))

    tamayoRain_result = tamayoRain_num1 * tamayoRain_num2
    print("The product is: ", tamayoRain_result )

    tamayoRain_ans = input("Do you want to calculate another one? (yes - y / no - n): ")
    print("_____________________________________________")
