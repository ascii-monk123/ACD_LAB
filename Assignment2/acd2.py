import math
#question for cfg for a^nb^n
stack=['\0']
#the transition functions for the pda
#transitions are like this curstate:('input symbol','stack top','operation','transition to which state')
currentState=0
pattern=''.center(20,'*')
def automatize(string):
    global currentState
    for index,char in enumerate(string):
        prevState=currentState
        print('Previous state is {}'.format(prevState))
        print(pattern)
        print('Input symbol is {}'.format(char))
        print(pattern)
        if char in ['a','b']:
            if index+1<=len(string)//2:
                print('Pushing into the stack')
                print(pattern)
                stack.append(char)
            else:
                lastEle=stack.pop()
                if char==lastEle:
                    print('Top of the stack equal to the sybmol {} . So performing pop operation'.format(char))
                    print(pattern)
                    currentState=2
                    
                else:
                    print('Top of the stack not  equal to the sybmol {} . So quitting'.format(char))
                    print(pattern)
                    currentState=3
                    break
        else:
            print('Invalid symbols in the string')
            break
        print('Current state is {}\n\n'.format(currentState))
        print(pattern)
    if currentState==2:
        print('String is a palindrome')
    else:
        print('String is not a palindrome')

string=input('Enter the required string which is to be tested for a palindrome : ')
if(len(string)%2==0):
    print('Even Palindrome\n')
    automatize(string)
    
else:
    print('Odd palindrome\n')
    newstring=string[:math.floor(len(string)/2)]+string[math.floor(len(string)/2)+1:]
    automatize(newstring)

    