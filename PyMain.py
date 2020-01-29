import subprocess
from subprocess import Popen, PIPE

caseOut={
  'N': 'N-Текущая координата',
  'W': '2-Сделать измерение маха',
  'M': '3-получить измерение маха',
  'C': '4-обнулить данные'
}

def func(arg):
  if arg=='N':
        print(p.stdin.readline().strip())
  if arg=='M':
        k = int(p.stdin.readline().strip())
        time = []
        coordinate = []
        while k > 0:
             coordinate.append(int(p.stdin.readline().strip()))
             time.append(float(p.stdin.readline().strip()))
             k=k-1
        return coordinate,time

global p
p = subprocess.Popen(["CRead","Read.C"], stdout=PIPE, stdin=PIPE)
print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
value = input()
while not (value in caseOut):
      print('такой операции нет,попробуйте еще раз')
      print('N:-Текущая координата,W-Сделать измерение маха,M-получить измерение маха,C-обнулить данные')
      value = input()
print(caseOut[value])
p.stdout.write(bytes(value + '\n', 'UTF-8'))
func(value)
