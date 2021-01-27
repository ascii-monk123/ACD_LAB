import re
grammar=input('Enter the grammer which has to be found')
if re.search('->',grammar):
    print('This is not a valid grammar. A valid grammar must have -> in it')
else:
    print('Seems like the grammer is valid but now just let us test it')
    