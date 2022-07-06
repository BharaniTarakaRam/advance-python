import re

patter='^r......r$'
test_patter='ramkumar'
result=re.match(patter,test_patter)
if result:
    print("search successful.")
else:
    print("search unsuccessful.")
#output: search successful.


import re

patter='^r......r$'
test_patter='ramkuma'
result=re.match(patter,test_patter)
if result:
    print("search successful.")
else:
    print("search unsuccessful.")

#output: search unsuccessful.




# for string only [a,b,c]
import re

str="hello world python is good programing lang"
result=re.match(r"[abc]",str)
print(result)
#output is none
#the output none because re.match() is searching only starting letter A so the output was none



#match funnction
import  re
str="all film titanic was released in 1998"
result=re.match(r"[abc]",str)
print(result)

# output <re.Match object; span=(0, 1), match='a'>
#it showing that the first_letter was A in str so the match A showing in output



#search function
import re
str="Hello class today the call is about python"
result=re.search(r"[abcef]",str)
print(result)

# output:<re.Match object; span=(1, 2), match='e'>
# re.search means it seach the str hole where it find match it's show's in output



#findall() function
import  re
str="111 film titacnic was released in 1998"
result=re.findall(r"[abc]",str)
print(result)

#output ['a', 'c', 'c', 'a', 'a'] it showing the match letter [abc]




#split Function
txt="nine player in kho-kho team"
result=re.split("\s",txt)
print(result)
#output:['nine', 'player', 'in', 'kho-kho', 'team']


#split function specify txt number
txt="nine player in kho-kho team"
x = re.split("\s", txt, 1)
print(x)
#output:['nine', 'player in kho-kho team']



# sub function
import re

txt="nine player in kho-kho team"
x = re.sub("\s", "9", txt)
print(x)

#output:nine9player9in9kho-kho9team

#sub function specify txt number
txt="nine player in kho-kho team"
x = re.sub("\s", "9", txt, 2)
print(x)

#output:nine9player9in kho-kho team


#.function

import re
str="ac"
result=re.search(r'..',str)
print(result)
#output:<re.Match object; span=(0, 2), match='ac'>

import re
str="abcd"
result=re.findall(r'..',str)
print(result)
#output:['ab', 'cd']

import re
str="abcdef"
result=re.findall(r'..',str)
print(result)
#output:['ab', 'cd', 'ef']

#[] Metacharacters
# to fine a set of characters
import re

txt = "The rain in India"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)
#outPut:['h', 'e', 'a', 'i', 'i', 'd', 'i', 'a']

# \ Metacharacters
#Signals a special sequence (can also be used to escape special characters)
import re

txt = "1 dollars in india is 75 rs "

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

#output:['1', '7', '5']

# ^ Metacharacters
# start with letter/name

import re

txt = "hello RAM"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
#Yes, the string starts with 'hello'

import re

txt = "hello RAM"

# Check if the string starts with 'hello':

x = re.findall("^h", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
#Yes, the string starts with 'hello'

# $ Metacharacters
# ending with letter/ name

import re

txt = "hello RAM"

# Check if the string starts with 'hello':

x = re.findall("h$", txt)
if x:
    print("Yes, the string ends with 'hello'")
else:
    print("No match")

#output:No match

import re

txt = "hello RAM"

# Check if the string starts with 'hello':

x = re.findall("RAM$", txt)
if x:
    print("Yes, the string ends with 'hello'")
else:
    print("No match")

#Yes, the string ends with 'hello'

# * Metacharacters
#Zero or more occurrences of a patter left to it
import re

txt = "hello Ram"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("...*o", txt)

print(x)


import re

txt = "hello Ram"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "m":

x = re.findall(".*m", txt)

print(x)



# + Metacharacters
#One or more occurrences of a patter left to it

import re

txt = "hello Ram"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("...+o", txt)

print(x)



import re

txt = "hello Ram"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "m":


x = re.findall(".+m", txt)

print(x)

# ? Metacharacters
#Zero or one occurrences of a patter left to it

import re

txt = "hello ram"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


# {} Metacharacters
#	Exactly the specified number of occurrences
import re

txt = "hello ram"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("r.{1}m", txt)

print(x)

# | Metacharacters
#	Either or

import re

txt = "The rain in india falls mainly the months of july and August!"

#Check if the string contains either "falls" or "mainly":

x = re.findall("falls|mainly", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


  import re

  txt = "The rain in india falls mainly the months of july and August!"

  # Check if the string contains either "falls" or "mainly" or "in":

  x = re.findall("(falls|mainly|in) the months of", txt)

  print(x)

  if x:
      print("Yes, there is at least one match!")
  else:
      print("No match")

import re

txt = "The rain in india falls mainly the months of july and August!"

#Check if the string contains either "may" or "are":

x = re.findall("may|are", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\A	Returns a match if the specified characters are at the beginning of the string

import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")



import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\Arain", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\Athe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\b	Returns a match if the specified characters are at the end of the string

import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall(r"st\b", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall(r"onth\b", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
import re

txt = "The rain in India"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#['ain']
#Yes, there is at least one match!



#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\d	Returns a match where the string contains digits (numbers from 0-9)
import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

 #outpu:[] no macth

import re
txt = "The rain in india falls mainly the months of 07 and 08!"
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

#['0', '7', '0', '8']
#Yes, there is a match!

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\D	Returns a match where the string DOES NOT contain digits

import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#output :['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'i', 'n', 'd', 'i', 'a', ' ', 'f', 'a', 'l', 'l', 's', ' ', 'm', 'a', 'i', 'n', 'l', 'y', ' ', 't', 'h', 'e', ' ', 'm', 'o', 'n', 't', 'h', 's', ' ', 'o', 'f', ' ', 'j', 'u', 'l', 'y', ' ', 'a', 'n', 'd', ' ', 'A', 'u', 'g', 'u', 's', 't', '!']

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\s	Returns a match where the string contains a white space character

import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#Yes, there is a match!


#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\S Returns a match where the string DOES NOT contain a white space character

import re
txt = "The rain in india falls mainly the months of july and August!"
x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'i', 'n', 'd', 'i', 'a', 'f', 'a', 'l', 'l', 's', 'm', 'a', 'i', 'n', 'l', 'y', 't', 'h', 'e', 'm', 'o', 'n', 't', 'h', 's', 'o', 'f', 'j', 'u', 'l', 'y', 'a', 'n', 'd', 'A', 'u', 'g', 'u', 's', 't', '!']
#Yes, there is a match!



#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

import re
txt = "The rain in india falls mainly the months of july and August! 07 AND 08 07_08"
x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'i', 'n', 'd', 'i', 'a', 'f', 'a', 'l', 'l', 's', 'm', 'a', 'i', 'n',
 #  'l', 'y', 't', 'h', 'e', 'm', 'o', 'n', 't', 'h', 's', 'o', 'f', 'j', 'u', 'l', 'y', 'a', 'n', 'd', 'A', 'u', 'g',
 #  'u', 's', 't', '0', '7', 'A', 'N', 'D', '0', '8', '0', '7', '_', '0', '8']
 # Yes, there is a match!

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\w Returns a match where the string DOES NOT contain any word characters
import re

txt = "The rain in india falls mainly the months of july and August! 07 AND 08 07_08"
x = re.findall("\W", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")

#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ', ' ']
#Yes, there is a match!

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#\Z Returns a match where the string last/end word characters
import re
txt = "The rain in india falls mainly the months of july and August"
x = re.findall("August\Z", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")
#output
#['August']
#Yes, there is a match!

import re
txt = "The rain in india falls mainly the months of july and August"
x = re.findall("july\Z", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")

#output
# []
# No match