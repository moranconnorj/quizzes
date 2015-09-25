"""wk1.4
warm-up
Instructions: For each of the following problems, fill out the answer underneath and
submit the finished quiz to me via personal slack message. You may consult your notes 
but please do not use the internet."""

#assign the number 8 to a variable eight.
eight = 8
#set b equal to eight.
b = eight
#print b.
print(b)
#Write a boolean expression that will return true if x is 'a' or 'b' and false otherwise.
if x is 'a' or x is 'b':
	return True
else:
	return False
#Write a boolean expression that returns true if and only if x is greater than ten and x is odd.
if x > 10 and x % 2 == 1:
	return True
else:
	return False
#write a function that takes a parameter, n, and then returns n (unchanged).
def get_n(n):
	return n
#write a function that takes a string, str_, and prints the string three times (once per line).
def print_string(str_):
	for x in range(3):
		print(str_)
#Write a program to prompt the user for hours and rate per hour to compute gross pay.
def gross_pay():
    hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    pay = float(hours) * float(rate)
    print("Pay: " + str(pay))
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
#given a str1 = "Hello " and a str2 = "World", how can we concatenate (join together) str1 to str2mul?
str1 + str2
#given a str1 = "Hello", how can we index str1 to get the 'o'? Give two different ways.
str1[-1]

lst = []
for x in str1:
	lst.append(x)
return lst[4]
#given a str1 = "Hi", what operation can we do to the string to output "HiHiHiHi"?
str1 * 4
#make a list, lst, containing the numbers 0 through 10.
lst = []
for x in range(11):
	lst.append(x)
#append the string 'hi' to the list
lst.append('hi')
#remove the 4 from the lst
lst.remove(4)
#how can you check if 5 is in the lst (your expression should return True if 5 is in the lst, and False otherwise)
5 in lst
#write a loop that prints each element from 0 through 9
for x in range(10):
	print(x)
#write a loop that prints each element from your lst.
for x in lst:
	print(x)
write a loop that prints out the element multiplied by two for each element from 0 through 9.
for x in range(10):
	print(x * 2)
#write a loop that will count from 0 to infinity.
x = 1
while x:
	x += 1
#write a statement that checks if a variable var is empty.
not var
#make a tuple containing a single element 'a'
('a',)
#make a tuple containing two elements, 'a' and 'b'
('a', 'b')
given a tuple containing 'Dicaprio' and 43, unpack the tuple with the variables name and age.
make an empty dictionary, dct.
add the key value pairs 'one'/1, 'two'/2, 'three'/3, 'four'/4
change the value of three to 'tres'
delete the key value pair 'two'/2.
write the following loops over dct:
a loop that gets the keys
a loop that gets the values
a loop that prints the key value pairs (not tuple)
a loop that prints tuples of the key value pairs.
why might we use a dictionary over a list of tuples?
Give a definition of the following:
mutability/immutability
homogeneous/heterogenous datatypes
overflow
abstraction
modularization
For each of the following datatypes, write M for mutable or I for immutable, HO for homogeneous or HE for heterogenous: ex. blub: MHO (note blub is not a datatype we will be going over in this class)
string
list
tuple
dictionary
what is the difference between printing output from a function vs. returning output from a function?