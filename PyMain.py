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

def getDataCoordinate():
        if(init):
                p = subprocess.Popen(["CRead","Read.C"], stdout=PIPE, stdin=PIPE)               
                init=False
        int l = int(p.stdin.readline().strip())
        return l
      
def getDataSensor():
        if(init):
                p = subprocess.Popen(["CRead","Read.C"], stdout=PIPE, stdin=PIPE)               
                init=False
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
          
 
print('N,W,M,C')
value=input()
checkSyntax(value)
time = []
coordinate = [] 
if(value='N'):
         time,coordinate = getDataSensor()
if(value='W'):
         int k = getDataCoordinate()
         print(k);


                 
                 
