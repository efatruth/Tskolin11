import time
import datetime
time.time()
time_now = datetime.datetime.fromtimestamp(
        int(time.time())
    ).strftime('%d-%m-%Y %H:%M:%S')


temp = "05-01-2018 09:21:20"


print('Tími núna --> {}, Tíma tékkaður{}'.format(time_now,temp))

if datetime.date(temp) > datetime.date(time_now):
    print('petur er faggi')

if datetime.date(temp) < datetime.date(time_now):
    print('petur er meiri faggi')