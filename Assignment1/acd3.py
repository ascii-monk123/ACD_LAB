reqString=input('Enter the string you want to test : ')
states=[0,1,2,3]
transitions={
    0:(1,0,0), #of the form state =>(transition for a,transition for b,output at incoming transition on q)
    1:(1,2,0),
    2:(1,3,0),
    3:(1,0,1),
}
currentState=0
noofabb=0
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
    output=transitions[currentState][2]
    print('Jumped to state : q{}'.format(currentState))
    print('Output is : {}'.format(output))
    if output==1:
        noofabb+=1
    print(''.center(20,'*'))
if(not acceptable):
    print('Invalid input string')
else:
    print('Number of abb in the given string are : {}'.format(noofabb))
print(''.center(20,'*'))