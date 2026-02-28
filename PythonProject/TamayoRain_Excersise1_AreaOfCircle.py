#AREA OF CIRCLE
#TAMAYO, RAIN ANGEL G.


import math
tamayoRain_ans = "y"

print("Hello! We are going to calculate area of circle.")
print("_____________________________________________")

while tamayoRain_ans == "y":

    tamayoRain_radius = float(input("Enter the radius please: "))
    tamayoRain_area = math.pi * tamayoRain_radius * 2
    print("The value of circle is: ", tamayoRain_area)

    tamayoRain_ans = input ("Do you want to calculate another one? (yes - y / no - n): ")
print("_____________________________________________")
