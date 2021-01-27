reqString=input('Enter the string you want to test : ')
states=[0,1,2,3,4,5]
transitions={
    0:(3,1), #of the form state =>(transition for a,transition for b)
    1:(4,2),
    2:(5,0),
    3:(0,4),
    4:(1,5),
    5:(2,3)
}
currentState=0
acceptable=True
for alpha in reqString:
    print('Current state : q{}'.format(currentState))
    print('Input alphabet {}'.format(alpha))
    if(alpha=='a'):
        currentState=transitions[currentState][0]
    elif(alpha=='b'):
        currentState=transitions[currentState][1]
    else:
        print('Invalid character in string... Exiting')
        acceptable=False
        break
    print('Jumped to state : q{}'.format(currentState))
    print(''.center(20,'*'))
if(not acceptable):
    print('Invalid input string')
elif(currentState==0):
    print('String accepted')
else:
    print('String not accepted')
