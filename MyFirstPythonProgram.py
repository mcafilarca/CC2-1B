# Filarca, Melchizedek Carl A.
# BSCS 1B
pound = float(input('Pounds = '))
print('Pounds (lbs) = ', pound)
Kilograms = float(pound * 0.45359237)
print('Converted to Kilograms (kg) = %.2f' % Kilograms)
print('================================================')
miles = float(input('Mile = '))
print('Miles (mi) = ', miles)
kilometers = float(miles * 1.609344)
print('Converted to kilometers (km) = %.2f' % kilometers)
print('================================================')
fahrenheit = float(input('Fahrenheit = '))
print('Fahrenheit (°F) = ', fahrenheit)
C = float(fahrenheit - 32)
celsius = float(C / 1.8)
print('Converted to Celsius (°C) = %.2f' % celsius)
print('================================================')
a, b, c, d, e, f, g, h, i, j = 14, 23, 22, 15, 19, 21, 19, 16, 25, 20
print('Age of student 1 : ', a)
print('Age of student 2 : ', b)
print('Age of student 3 : ', c)
print('Age of student 4 : ', d)
print('Age of student 5 : ', e)
print('Age of student 6 : ', f)
print('Age of student 7 : ', g)
print('Age of student 8 : ', h)
print('Age of student 9 : ', i)
print('Age of student 10 : ', j)
AgeSum = (a + b + c + d + e + f + g + h + i + j)
AverageAge = float(AgeSum / 10)
print('Average Age of the Students is : ', AverageAge)
print('================================================')
string = ("""{Mc} used their Sword and their Strength to defeat the <{Enemy}>. <{SecondMc}> used their Bow and arrow and their <{Skill}> to defeat the <{Enemy}>.
Gimli used their Axe and their Wisdom to defeat the <{Enemy}>.Frodo used their <{Ability}> to defeat the <{Enemy}>.""".format(Mc='Aragorn', SecondMc='Legolas',
                                                Ability='Ring and Magic', Skill='Agility', Enemy='evil dragon'))
print(string)

