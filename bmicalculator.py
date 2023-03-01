weight = float(input('enter mass in kg:'))
height = float(input('enter height in meters:'))

bmi = weight / (height ** 2)
print('Your bmi is', bmi)
print('Your bmi classifies as:')

if bmi < 18.5:
    print('underweight')
elif bmi >= 18.5 and bmi < 25:
    print('normal weight')
elif bmi >= 25 and bmi < 30:
    print('overweight')
elif bmi >= 30 and bmi < 35:
    print('grade 1 obesity')
elif bmi >= 35 and bmi < 40:
    print('grade 2 obesity')
elif bmi >= 40:
    print('grade 3 obesity')
