import subprocess
from subprocess import Popen, PIPE

global p
global init 

Ops={
  'N': 'N',
  'W': 'W',
  'M': 'M',
  'C': 'C',
  'S': 'S'
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
        p.stdin.write(bytes('C' + '\n', 'UTF-8'))
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
        l = int(p.stdout.readline().strip())
        return l
    except:
        raise Exception('error')
        
        
def getDataArray():
    try:
        p.stdin.write(bytes('M' + '\n', 'UTF-8'))
        k = int(p.stdout.readline().strip())
        time = []
        coordinate = []
        while k > 0:
            coordinate.append(int(p.stdout.readline().strip()))
            time.append(float(p.stdout.readline().strip()))
            k=k-1
        return coordinate,time
    except:
        raise Exception('error')
        




def checkSyntax(arg):
        if not (arg in Ops):
            raise Exception('not found operation')
          
p = subprocess.Popen(["/home/pi/Pendulum/module"], shell=True,stdout=PIPE, stdin=PIPE)
print('N,W,M,C')
value=input()
time = []
coordinate = [] 
if(value=='N'):
        time,coordinate = getDataCoordinate()
if(value=='W'):
        k = getDataArray()
        print(k);
                 
