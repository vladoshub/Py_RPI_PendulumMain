import subprocess
from subprocess import Popen, PIPE

global p
global init=True

caseOut={
  'N': 'N-Текущая координата',
  'W': '2-Сделать измерение маха',
  'M': '3-получить измерение маха',
  'C': '4-обнулить данные'
}

def getData(arg):
  if arg=='N':
        int l = int(p.stdin.readline().strip())
        return l
  if arg=='M':
        int k = int(p.stdin.readline().strip())
        time = []
        coordinate = []
        while k > 0:
             coordinate.append(int(p.stdin.readline().strip()))
             time.append(float(p.stdin.readline().strip()))
             k=k-1
        return coordinate,time


        
 

def checkSyntax(arg):
        if not (arg in caseOut):
                raise Exception('not found operation')
          
          
def main(arg):
        checkSyntax(arg)
        time = []
        coordinate = []
        if(init):
                p = subprocess.Popen(["CRead","Read.C"], stdout=PIPE, stdin=PIPE)               
                init=False
         p.stdout.write(bytes(arg + '\n', 'UTF-8'))
         if(arg='N'):
                 time,coordinate = getData(arg)
                 return time,coordinate
         if(arg='W'):
                 int k = getData(arg)
                 return k
 
print('N,W,M,C')
value=input()      
time = []
coordinate = [] 
if(value='N'):
         time,coordinate = main(value)
if(value='W'):
         int k = main(value)
         print(k);


                 
                 
