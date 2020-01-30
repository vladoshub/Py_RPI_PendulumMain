import subprocess
from subprocess import Popen, PIPE

global p 
global init 

Ops={
  'N': 'N-Текущая координата',
  'W': 'W-Сделать измерение маха',
  'M': 'M-получить измерение маха',
  'C': 'C-обнулить данные'
  'S': 'S-изменить пороги чувствительнсои.1-MAX Отклонение от старта,2-MAX Отклонение от того на сколько маятник может отклоняться назад(вперед) при измерении'
}

def doChangeSensor(arg1,arg2):
    try:
        p.stdin.write(bytes('S' + '\n', 'UTF-8'))
        p.stdin.write(bytes(arg1 + '\n', 'UTF-8'))
        p.stdin.write(bytes(arg2 + '\n', 'UTF-8'))
    except:
        raise Exception('error')


def doClear():
    try:
        p.stdin.write(bytes('С' + '\n', 'UTF-8'))
    except:
        raise Exception('error')




def doMeasurement():
    try:
        p.stdin.write(bytes('W' + '\n', 'UTF-8'))
    except:
        raise Exception('error')



def getDataCoordinate():
    try:
        p.stdin.write(bytes('N' + '\n', 'UTF-8'))
        l = int(p.stdin.readline().strip())
        return l
    except:
        raise Exception('error')
        
        
def getDataArray():
    try:
        p.stdin.write(bytes('M' + '\n', 'UTF-8'))
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
        if not (arg in Ops):
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
                 
                 
