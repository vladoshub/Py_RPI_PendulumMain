from subprocess import Popen, PIPE

caseOut = {
'N': 'N-Текущая координата',
'W': '2-Сделать измерение маха',
'M': '3-получить измерение маха',
'C': '4-обнулить данные'
}

def func(arg):
if arg=='N':
print(p.stdout.readline().strip())
if arg=='M':
int k =int(p.stdout.readline().strip())
p.stdout.flush()
time = []
coordinate = []
while k > 0:
coordinate.append(int(p.stdout.readline().strip()))
p.stdout.flush()
time.append(int(p.stdout.readline().strip()))
p.stdout.flush()
k=k-1
return coordinate,time

global p
p = Popen(['bin:/Dekstop/Pendulum/Read.C'], shell=True, stdout=PIPE, stdin=PIPE)
print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
value = input()
while not (value in caseOut):
print('такой операции нет,попробуйте еще раз')
print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
value = input()
print(caseOut[value])
p.stdin.write(bytes(value + '\n', 'UTF-8'))
p.stdin.flush()
func(value)
