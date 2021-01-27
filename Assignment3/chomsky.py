import re
#here strings are considered to be alphabets and special characters not numbers
grammar=input("Enter the grammar which you want to check for CFG. Enter each production with space in between : ").split(" ")

def checkForType0(grammar):
    isValid=True
    for gram in grammar:
        if re.search(r'^([a-zA-Z]*[A-Z][a-zA-z]*->[a-zA-Z]*)$',gram):
            continue
        else:
            isValid=False
            break
    return isValid
def checkForType1(grammar):
    isValid=True
    for gram in grammar:
        left,right=gram.split('->')
        if gram=='S->#':
            continue
        if re.search(r'^([a-zA-Z]*[A-Z][a-zA-Z]*->[a-zA-Z]*[a-zA-Z]+[a-zA-Z]*)$',gram) and len(left)<=len(right):
            continue
        else:
            isValid=False
            break
    return isValid
def checkForType2(grammar):
    isValid=True
    for gram in grammar:
        
        if re.search(r'^([A-Z]->[a-zA-Z]*)$',gram):
            continue
        else:
            isValid=False
            break
    return isValid
def checkForType3(grammar):
    isValid=True
    for gram in grammar:
        if re.search(r'^([A-Z]->(([A-Z][a-z]*)|([a-z]*)|([a-z]*[A-Z])))$',gram):
            continue
        else:
            isValid=False
            break
    return isValid
if len(grammar)>=1:
    if checkForType3(grammar):
        print('It is type 3 grammar')
    elif checkForType2(grammar):
        print('It is type 2 grammar')
    elif checkForType1(grammar):
        print('Yes it is type 1 grammar')
    elif checkForType0(grammar):
        print('Yes it is a type 0 grammar')
    else:
        print('It is none of the 4 types of grammar')
    
else:
    print('Please enter at least one valid grammar')
    
