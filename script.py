# 1.Simple Message: Assign a message to a variable, and then print that message.
x = "Hello world!"
print(x)

#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something 
#like the following, including the quotation marks:
lesson_author = "MSJ"
Problems_are_part_of_life_facing_them_is_a_art_of_life = "MSJ"
x = "MSJ"
print(Mark)

#Calculate Area of a Circle: Write a Python program which accepts the radius of a circle from the user and compute the area.
Radius = float(input(" Enter radius of the circle: "))
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#Check Number either positive, negative or zero:: Write a Python program to check if a number is positive,
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")

#Vowel Tester Write a Python program to test whether a passed letter is a vowel or not
l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 

#BMI Calculator Write a Python program to calculate body mass index Program
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the 
#list, one at a time
name = ['Asad' , 'Huzaifa' ,  'Ali' , 'Razzaq' , 'Umar' , 'Ishaq']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

#Start with the list you used in Question 4, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
for friend in name:
    print(friend,"they are kamine friends")

#Make a python program that conatains your nine favourite dishes in a list called foods. Print the message, 
#The first three items in the list are:
foods = ['Pizza','burger','pizza','mommos','macroni','spheghetti','corn','nuggets','pasta']
print('The first three items in the list are',foods[0:3])
print('Three items from the middle of the list are',foods[3:6])
print('The last three items in the list are',foods[6:])

#Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods. Then, 
#do the following
#Add a new dish to the original list.
#Add a different dish to the list friend_foods.
#Prove that you have two separate lists
friends_food = foods[0:9]
foods.append("chicken roll")
friends_food.append("chapotla")
print(foods)
print(friends_food)

#Print the message, My favorite pizzas are: and then use a for loop to print the first list.
#Print the message
print("My favorite Burger are : ")
for items in foods:
    print(items)
