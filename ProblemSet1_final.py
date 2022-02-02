# -*- coding: utf-8 -*-
"""

edX MIT Python course assignments

Problem Set 1  :  These are the scripts for Unit 1 assignments

solutions by Manoj Menon 
31st Jan 2022

-----------------------------------------
  
Problem # 1 

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5


Solution for #1 """

# s= input('Enter a series of text characters in small case without gaps : ')
# s= 'ebobby'
s= 'ebouaiogiewy'
Numofvowels = 0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        Numofvowels += 1
print("Number of vowels: " + str(Numofvowels))


"""-------------------------------------------------

Problem # 2  

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2


Solution for #2  """

# s = input('Enter a series of text characters in small case without gaps : ')
# s = 'ebobby'
# s = 'abobdbobcobobe'
s = 'bobobobobob'
Numofbobs = 0
inputtext = s
inputtextlength = len(inputtext)
for pos in range((inputtextlength-2)):
    checktext = inputtext[pos]+inputtext[pos+1]+inputtext[pos+2]
    if checktext == 'bob':
        Numofbobs += 1
print("Number of times bob occurs is: " + str(Numofbobs))


"""-----------------------------------------------

Problem # 3  

Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc


Solution for  #3  """

# -----Logic for the code------
# 
# Start a loop at first char of input string and perform below operation for every next char:
#    Check if the ordinate value of current char is < next char
#       If it is, concatenate it to the longeststring variable
#       If it is not then store that longeststring as well as its length for next iteration, break out of that loop
#        and restart the check from the next char

# s = input('Enter a series of text characters without gaps : ')
# s = 'abcdefghijklmnopqrstuvwxyz'
# s = 'abcdef'
s = 'abcdbcde'
inputtext = s
inputtextlength = len(inputtext)
newlongeststring = inputtext[0]
finallongeststring =inputtext[0]
for pos in range(inputtextlength-1): 
    if ord(inputtext[pos]) <= ord(inputtext[pos+1]):
        newlongeststring += inputtext[pos+1]
        pos += 1
        finallongeststring1 = newlongeststring
    else:
        newlongeststring = inputtext[pos+1]
        pos += 1
    if len(newlongeststring) > len(finallongeststring):
        finallongeststring = newlongeststring 
print('Longest substring in alphabetical order is: ', finallongeststring)
              
