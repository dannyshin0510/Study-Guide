# This is a collection of commonly used regular expressions for string manipulation

import re # needed for regex

# re.findall()   	Returns a list containing all matches
# re.search()	    Returns a Match object if there is a match anywhere in the string
# re.split()	    Returns a list where the string has been split at each match
# re.sub()	        Replaces one or many matches with a string

txt = "The rain in Spain"

x = re.findall("ai", txt)
x = re.findall("Portugal", txt) #no match returns empty list

x = re.search("\s", txt)
x = re.search("Portugal", txt) #no match retuns None

x = re.split("\s", txt)
x = re.split("\s", txt, 1) #only do it at the first occurance

x = re.sub("\s", "9", txt)
x = re.sub("\s", "9", txt, 2) #first 2 occurences


