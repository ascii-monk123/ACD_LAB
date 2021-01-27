#question for cfg for a^nb^n
stack=['\0']
#the transition functions for the pda
#transitions are like this curstate:('input symbol','stack top','operation','transition to which state')
transitions={
    0:[('a','\0','push',0),('a','a','push',0),('b','\0','none',3),('b','a','pop',1)],
    1:[('a','\0','none',3),('a','a','none',3),('b','a','pop',1),('\0','\0','none',2),('b','\0','none',3)],
}
pattern=''.center(20,'*')
curState=0
def alterStack(operation,char):
    global stack
    if operation=='push':
        stack.append(char)
    elif operation=='pop':
        stack.pop()
    else:
        pass

def makeTransition(char):
    global curState
    print(pattern)
    print('Current symbol is :')
    if char!='\0':
        print(char)
    else:
        print('String terminal')
    print(pattern)
    print('Cur state {}'.format(curState))
    print(pattern)
    stackTop=stack.pop()
    print('Stack top is :')
    if stackTop!='\0':
        print(stackTop)
       
    else:
        print('Null')
    print(pattern)
        
    stack.append(stackTop)
    if curState==3:
        return
    elif curState<2:
        for tup in transitions[curState]:
            if tup[0]==char and tup[1]==stackTop:
                alterStack(tup[2],char)
                curState=tup[3]
                break
    elif curState==2 and char !='\0':
        curState=3
    print('After transition state is {}'.format(curState))
    print('\n\n')
testString=input('Enter the string (must have either a or b) : ')
testString+='\0'
print(testString)
for char in testString:
    if char in ['a','b','\0']:
        makeTransition(char)
    else:
        print('Sorry unwanted symbol inside the input string')
        break
if curState==2:
    print('String accepted by the pda')
else:
    print('String not accepted')