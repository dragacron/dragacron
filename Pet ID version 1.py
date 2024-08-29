#this code is my first code ever. I am using input variables, if else statements and the "print" command.
#the function of this code is to state the name of the pet that 
# meets the description given by the user when prompted by the program.

#requires answers to be lowercase with no spaces.

#determines value of 'pet'
pet = input('What kind of pet is it? ')

#sequence followed if user answers cat:
if pet == 'cat':
 #asks user to define the catColor
 catColor = input('What color is the cat? ')
 if catColor == 'orange':
  #cat name if catColor is orange.
  print("It's Tux!")
 elif catColor == 'black':
  #cats name if catColor is black.
  print("It's Keebs!")
 else:
  #output if user is speaking of any cat besides Keebler and Tux:
  print("I don't know this cat.")

#sequence followed if user answers dog:
if pet == 'dog':
 #asks user to define dogColor
 dogColor = input('What color is the dog? ')
 if dogColor == 'orange':
  #dog's name if users dog is orange:
  print("It's Niko!")
 elif dogColor == 'grey':
  #dog's name if users dog is grey:
  print("It's Cooper!")
 else:
  #output if user is speaking of any dog besides Niko and Cooper
  print("I don't know this dog.")

#sequence if user does not have a dog or cat.
if pet != 'cat' and pet != 'dog': 
 print("I only know 'dog' or 'cat.'")

#I would like to improve the code to be able to accept a wider tolerance of 
# answers and have a larger amount of output options. This program is very rigid as is.