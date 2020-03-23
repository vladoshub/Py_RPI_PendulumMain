import subprocess
from subprocess import Popen, PIPE
import measurement




Ops = {  # protol(протокол для общения с датчиком)
    'N': 'N',  # current coordinate
    'W': 'W',  # start Measurement
    'M': 'M',  # start Measurement
    'C': 'C',  # claer all safe data
    'S': 'S',  # overwrite sensitivity threshold
    'E': 'E',  # stop driver
    'T': 'T'  # get status driver
}


def doChangeSensor(arg1, arg2):  # overwrite sensitivity threshold(перезаписывает порог чувствительности)
    try:
        p.stdin.write(bytes('S\n', 'UTF-8'))
        p.stdin.flush()
        p.stdin.write(bytes(arg1 + '\n', 'UTF-8'))
        p.stdin.flush()
        p.stdin.write(bytes(arg2 + '\n', 'UTF-8'))
        p.stdin.flush()
    except:
        raise Exception('error')


def doClear():  # claer all safe data(очищает все измерения сделанные датчиким)
    try:
        p.stdin.write(bytes('C\n', 'UTF-8'))
        p.stdin.flush()
    except:
        raise Exception('error')


def doMeasurement():  # start Measurement(Запустить режим ожидания старта маятника и записи маха)
    try:
        p.stdin.write(bytes('W\n', 'UTF-8'))
        p.stdin.flush()
        status = p.stdout.readline().strip().decode()
        return status
    except:
        raise Exception('error')


def getStatus():  # get status driver(получает текущий режим работы драйвера)
    try:
        p.stdin.write(bytes('T\n', 'UTF-8'))
        p.stdin.flush()
        statusWork = p.stdout.readline().strip().decode()
        statusLastWork = p.stdout.readline().strip().decode()
        return statusWork, statusLastWork
    except:
        raise Exception('error')


def getDataCoordinate():  # current position(возвращает текущее положение маятника)
    try:
        p.stdin.write(bytes('N' + '\n', 'UTF-8'))
        p.stdin.flush()
        l = int(p.stdout.readline().strip().decode())
        return l
    except:
        raise Exception('error')


def getDataArray():  # get received data-time and coordinate(возвращает собранные данные в виде 2х массивов-время и коррдинату)
    try:
        p.stdin.write(bytes('M\n', 'UTF-8'))
        p.stdin.flush()
        status = p.stdout.readline().strip().decode()
        meas = measurement.measurement()
        meas.set_Status(status)
        k = int(p.stdout.readline().strip().decode())
        k=k-1
        meas.set_Count(k)
        if (status == 'I' and k > 0):
            meas.set_Count(k)
            time = []
            coordinate = []
            while k > 0:
                time.append(float(p.stdout.readline().strip().decode()))
                coordinate.append(int(p.stdout.readline().strip().decode()))
                k = k - 1
            meas.set_Time(time)
            meas.set_Coordinate(coordinate)
            return meas
        else:
            return meas
    except:
        raise Exception('error')


def checkSyntax(arg):
    if not (arg in Ops):
        raise Exception('not found operation')


def init():  # start driver(запускает драйвер который опрашивает датчик.без этого ничего работать не будет)
    try:
        global p
        p = subprocess.Popen(["sudo","/home/pi/Pendulum/module"], stdout=PIPE, stdin=PIPE)
        return True
    except:
        return False


def stop():  # stop driver(останавливает драйвер)
    try:
        p.stdin.write(bytes('E\n', 'UTF-8'))
        p.stdin.flush()
    except:
        raise Exception('error')
