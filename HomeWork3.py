from MyModuls.moduls import *
import os
import datetime

def kill(src, file_name):
    '''
    Функция принемает в аргумент путь к папке
    в которой находиться файл который нужно удалить,
    второй аргумент имя файла с расширением.
    '''
    os.chdir(src)
    l = os.listdir('.')
    for i in l:
        if os.path.isfile(i):
            print(i)
            if i == file_name:
                os.remove(file_name)
        else:
            kill(i, file_name)
            os.chdir('../')

print(kill('.', 'txt.txt'))


while True:
    now = datetime.datetime.now()   # показывает время
    time.sleep(1)   # задержка в 1 секунду
    print(now)
