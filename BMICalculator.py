# Simple BMI Calculator

mass = float(input('Enter your weight (in kg): ')) # weight in kg
height = float(input('Enter your height (in m): ')) # height in m

bmi = mass / height ** 2
print(bmi)