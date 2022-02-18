'''name = input('what is your name?')
print('hello  ' + name)'''

#####

'''name = 'Ahmed' # string
age = 13 # integer
pi = 3.14 # float
cars = ['bmw', 'mercedes', 'range rover'] # list 
print (name)
print (age)
print (cars)
print (pi)''' 

####
'''first_name = 'jmaila '
Surname = 'Ali'

full_name = first_name.capitalize() + '' + Surname
print (full_name)
print (len(first_name))
print (full_name.endswith('Ali'))'''

####
'''addition = 12 + 5 
print (addition )
subtraction = 200 - 50
print (subtraction )
multiply = 5*5
print (multiply)
mod = 10 % 3 ## how many 3 goes to 10 = 3 and 1 is remanider
print (mod)

#####
print (10 <= 10)
print (0==0)
print (15 > 5)'''

########
'''is_adult = False 
age = 20
if is_adult:
    print ('is_adult')

if age >= 18:
     print ('adult')
else:
    print ('teenager')'''


######## list 
'''cars = ['bmw', 'tesla', ' jeb', 'toyota', 'honda'  ]
print (len(cars)) 
print (cars)
print (cars[1])
print(cars[2])'''
 
#### loops
'''cars = ['bmw', 'tesla', 'jeb', 'toyota', 'honda'  ]
for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
      print (car.capitalize())'''

#### while loop 
'''number = 0
while number <= 10:
    print (number)
    number = number + 1 
else:
    print ('while ended and value of number is ' + str(number))'''


#### functions 

'''def check_age(age):
    if age < 15:
        print ('not an adult')
    else:
        print ('i am adult')
    

print('hello'.endswith('o'))
check_age(15)
check_age(13)
check_age(16)'''


##### classes
'''class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

jhon = Person('jhon', 22)
mariam = Person ('mariam', 18)
print (jhon.name + ' ' + str(jhon.age))
print (mariam.name + ' ' + str(mariam.age))'''

### classes and BehViours 

'''class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def walk (self):
        print (self.name + 'is walking.... ')
    def speak (self):
        print ('Hello my name is ' + self.name + ' and I am ' + str(self.age) + 'years old ')

jhon = Person('jhon', 22 )
mariam = Person ('mariam', 18 )
print (jhon.name + ' ' + str(jhon.age ))
jhon.speak ()
jhon.walk ()
print (mariam.name + ' ' + str(mariam.age ))
mariam.speak ()
mariam.walk ()'''   

####### other style 

''' class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def walk (self):
        print (self.name + ' is walking.... ')
    def speak (self):
        print (' Hello my name is ' + self.name + ' and I am ' + str(self.age ) + ' years old ')

jhon = Person('jhon', 22 )
jhon.speak ()
jhon.walk ()

print('----------------------------')

mariam = Person ('mariam', 18 )
mariam.speak ()
mariam.walk ()'''  

##### create documents 

# adding a picture in cv 








