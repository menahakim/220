# program will ask the user to input how many numbers will be evaluated
# after the user inputs the numbers I will use a for loop  to determine the mean
# using the different formulas
import math

values_tbe = eval(input("Enter the values to be entered:"))

sumvariable = 0
harmonic = 0
geometric = 1

for i in range(values_tbe):
    value = eval(input("Enter value: "))
    sumvariable = value**2 + sumvariable
    rms_step1 = sumvariable / values_tbe
    harmonic = harmonic + (1 / value)
    geometric = geometric * value

rms_average = math.sqrt(rms_step1)
harmonic_average = values_tbe / harmonic
geometric_average = math.pow(geometric, 1 / values_tbe)

print(round(rms_average, 3))
print(harmonic_average)
print(round(geometric_average, 3))






