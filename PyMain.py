import subprocess
from subprocess import Popen, PIPE

global p
global init

caseOut={
  'N': 'N-Текущая координата',
  'W': '2-Сделать измерение маха',
  'M': '3-получить измерение маха',
  'C': '4-обнулить данные'
}

def getDataCoordinate():
    try:
        l = int(p.stdin.readline().strip())
        return l
    except:
        raise Exception('error')
        
        
def getDataSensor():
    try:
        k = int(p.stdin.readline().strip())
        time = []
        coordinate = []
        while k > 0:
            coordinate.append(int(p.stdin.readline().strip()))
            time.append(float(p.stdin.readline().strip()))
            k=k-1
        return coordinate,time
    except:
        raise Exception('error')
        
def init():
    p = subprocess.Popen(["CRead","Read.C"], stdout=PIPE, stdin=PIPE) 



def checkSyntax(arg):
        if not (arg in caseOut):
            raise Exception('not found operation')
          
 
print('N,W,M,C')
value=input()
checkSyntax(value)
init()
time = []
coordinate = [] 
if(value=='N'):
        time,coordinate = getDataSensor()
if(value=='W'):
        k = getDataCoordinate()
        print(k);
                 
                 
