#!/usr/bin/env python3

"""
63d401e2c0042dc0606ae494b08cb9b8
python
lab1
v2
chai17
2017-08-09 18:47:11
v2.3.3 (2017-06-12)

Generated 2017-08-09 20:47:12 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""


from dbwebb import Dbwebb

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 73.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_one = 73



ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 74. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_two = 74
result = num_two + num_one



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 45.
#
# Create another variable called `num_four` and give it the value 39.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 45
num_four = 39
result = (num_four - num_three) +result




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = num_one * num_three




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 81.61.
#
# Create another variable called `float_two` and give it the value 73.63.
#
# Sum the two values and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

float_one = 81.61
float_two = 73.63

result = float_one + float_two


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = (((num_three + num_one) - num_four) * num_two) + float_two - float_one




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'storage' and 'icecream'
# and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
str1 = "storage"
str2 = "icecream"
konkatenera = str1 + str2




ANSWER = konkatenera

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'icecream' with the integer 73 with a space between
# the two variables and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

konkatenera = str2 + " " + str(num_one)




ANSWER = konkatenera

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 73 with the word 'storage' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 74 and the word 'icecream' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#

konkatenera = str(num_one) + " " + str1
konkatenera = konkatenera + " and " + str(num_two) + " " + str2




ANSWER = konkatenera

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#
string_number = str(30)
actual_number = 5

result = int(string_number) / actual_number


ANSWER = round(result)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Two large and one small pumps can fill a swimming pool in four hours. One
# large and three small pumps can also fill the same swimming pool in four
# hours. How many minutes will it take four large and four small pumps to
# fill the swimming pool?
#
# (We assume that all large pumps are similar and all small pumps are also
# similar.)
#
# Answer with the number of minutes.
#
# Write your code below and put the answer into the variable ANSWER.
#
hours = 4
minutes = 60 * hours
large = 0.4
small = 0.2
speed = (large * 4) + (small * 4)

endtime = minutes / speed


ANSWER = round(endtime)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anders has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format: 'Peter calls from [#Peter's phonenumber] to Anders on
# [#Anders's phonenumber] for [#hours] hours every year.' Replace the content
# inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#
sundays = 52
peterPhone = "0731415926"
andersPhone = "0727182818"
callTime = 9
hoursYear = (sundays * callTime) / 60
konkatenera = "Peter calls from " + peterPhone + " to Anders on " + andersPhone\
 + " for " + str(hoursYear) + " hours every year."




ANSWER = konkatenera

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
