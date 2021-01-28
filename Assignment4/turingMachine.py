#turing machine for a^nb^n-2 n>=2
symbolSet={'a','b','null','h'}
inpString=input('Enter the string which you want to test in the turing machine e=>{a,b} : ')
tape=[]
tape.extend([char for char in inpString]+['null'])
curState=0
curTapeIndex=0
transitions={
    0:[('a','x','r',1)],
    1:[('a','a','r',1),('b','y','l',2),('null','null','l',3),('y','y','r',1)],
    2:[('a','a','l',2),('y','y','l',2),('x','x','r',0)],
    3:[('a','a','l',3),('y','y','l',3),('x','x','r',4)],
    4:[('a','a','r',5)],
    5:[('y','y','r',5),('null','null','l','HALT')],
    'HALT':[]
}
def MoveLeftOnTape():
    global curTapeIndex
    curTapeIndex-=1
def MoveRightOnTape():
    global curTapeIndex
    curTapeIndex+=1

def performTransitions(symbol):
    global curTapeIndex
    global curState
    transitionExists=False
    for tuple in transitions[curState]:
        if tuple[0]==symbol:
            transitionExists=True
            print('\n')
            print('Input symbol is : {} '.format(symbol))
            print('Moving from state q{} to state q{}'.format(curState,tuple[3]))
            print('Replace tape index : {} with {}'.format(curTapeIndex,tuple[1]))
            curState=tuple[3]
            tape[curTapeIndex]=tuple[1]
            if tuple[2]=='l':
                MoveLeftOnTape()
                print('Moving Left')
            elif tuple[2]=='r':
                MoveRightOnTape()
                print('Moving Right')
            
            break
    return transitionExists

while(curState!='HALT'):
    transitionExists=performTransitions(tape[curTapeIndex])
    if not transitionExists:
        print('Transition doesnt exist for {} on {}'.format(tape[curTapeIndex],curState))
        print('String Rejected')
        break

if curState=='HALT':
    print('String accepted by the turing machine')
else:
    print('String not accepted by the turing machine')

