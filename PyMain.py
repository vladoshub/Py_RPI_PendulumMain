from subprocess import PIPE
import sys

caseOut = {
'N': 'N-Текущая координата',
'W': '2-Сделать измерение маха',
'M': '3-получить измерение маха',
'C': '4-обнулить данные'
}

def func(arg):
if arg=='N':
print(sys.stdin.readline().strip())
if arg=='M':
int k =int(sys.stdin.readline().strip())
time = []
coordinate = []
while k > 0:
coordinate.append(int(sys.stdin.readline().strip()))

time.append(float(sys.stdin.readline().strip()))

k=k-1
return coordinate,time

global p
p = subprocess.run(['bin:/Dekstop/Pendulum/Read.C'], shell=True, stdout=PIPE, stdin=PIPE)
print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
value = input()
while not (value in caseOut):
print('такой операции нет,попробуйте еще раз')
print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
value = input()
print(caseOut[value])
sys.stdout.write(bytes(value + '\n', 'UTF-8'))
func(value)
