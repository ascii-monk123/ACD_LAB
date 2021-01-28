#turing machine for a^nb^n-2 n>=2
symbolSet={'a','b','null','h'}
inpString=input('Enter the string which you want to test in the turing machine e=>{a,b} : ')
tape=['null']
tape.extend([char for char in inpString]+['null'])
curState=0
curTapeIndex=0
transitions={
    0:[('null','null','r',0),('h','h','r',0),('a','h','r',1)],
    1:[('h','h','r',1),('a','a','r',1),('b','h','l',2),('null','null','l',3)],
    2:[('a','a','l',2),('h','h','l',2),('null','null','r',0)],
    3:[('a','h','l',4),('h','h','l',3)],
    4:[('a','a','r',5),('h','h','l',4),('null','null','r','HALT')]
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

while(curState!=5 and curState!='HALT'):
    transitionExists=performTransitions(tape[curTapeIndex])
    if not transitionExists:
        print('Transition doesnt exist for {} on {}'.format(tape[curTapeIndex],curState))
        print('String Rejected')
        break

if curState=='HALT':
    print('String accepted by the turing machine')
elif curState==5:
    print('String not accepted by the turing machine')

