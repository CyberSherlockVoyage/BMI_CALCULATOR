height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = int(weight)

BMI = new_weight / new_height ** 2

BMI_as_int = int(BMI)
second_BMI_as_int = str(BMI_as_int)

print("Your BMI is: " + second_BMI_as_int)
