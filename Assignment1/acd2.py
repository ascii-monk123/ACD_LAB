reqString=input('Enter the string you want to test : ')
states=[0,1,2,3,4]
transitions={
    0:(1,0), #of the form state =>(transition for a,transition for b)
    1:(2,0),
    2:(2,3),
    3:(1,4),
    4:(4,4)
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
elif(currentState==4):
    print('String not accepted')
else:
    print('String accepted')

