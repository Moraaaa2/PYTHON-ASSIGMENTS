# https://elzero.org/python-assignments-lesson-from-11-to-18/


# 1

Name = 'omar'
Age = 19
Country = 'EGYPT'

print(f'''
"Hello '{name}', How You Doing \ """ Your Age Is "{Age}"" + And Your Country Is: {Country}
''')

#2

print(f'''
"Hello '{name}', How You Doing \\\n """ Your Age Is "{Age}"" +\n And Your Country Is: {Country}
''')

#3

name = 'Elzero'

print(name[1])
print(name[2])
print(name[-1])

#4

print(name[1:4]) #lze
print(name[::2]) #Ezr
print(name[-2]+name[2]+name[0]) #rzE

#5

name = "#@#@Elzero#@#@"

print(name.strip("#@"))

#6

num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

#7

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20 , '@'))
print(name_two.rjust(20 , '@'))

#8

name_one = "OSamA"
print(name_one.swapcase())
name_two = "osaMA"
print(name_two.swapcase())

#9

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))

#10

name = "Elzero"
print(name.index('z'))

#11

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace('<3' , 'Love' , 1))

#12

print(msg.replace('<3' , 'Love' ))

#13

name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
