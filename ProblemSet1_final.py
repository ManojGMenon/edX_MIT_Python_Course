# -*- coding: utf-8 -*-
"""
Problem Set 1  :  These are the scripts for Unit 1

solutions by Manoj Menon 
31st Jan 2022

"""

""" Problem # 1 """

# s= input('Enter a series of text characters in small case without gaps : ')
# s= 'ebobby'
s= 'ebouaiogiewy'
Numofvowels = 0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        Numofvowels += 1
print("Number of vowels: " + str(Numofvowels))



"""   Problem # 2  """

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



"""   Problem # 3  """

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
        
        
