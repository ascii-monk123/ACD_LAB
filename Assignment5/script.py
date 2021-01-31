#this comment shall not be written
import re
class Grep():
    def __init__(self,exp,filename) -> None:
        self.filename=filename
        self.exp=exp
    def no_of_lines_matched(self)->int:
        count=0
        try:
            fhand=open('{}.txt'.format(self.filename))
            for line in fhand:
                line=line.rstrip()
                if(re.search('{}'.format(self.exp),line)):
                    count+=1
            return count
        except:
            return None

regExp=input('Enter the required regular expression : ')
filename=input('Enter the filename : ')
grep=Grep(regExp,filename)
number=grep.no_of_lines_matched()
if(number):
    print('The number of lines that match the given regular expression are {}'.format(number))
else:
    print('There was an error reading the  files')