import time

print('{0} сек с 1янв1970'.format(time.time()))
print('{0} текущее время UTC'.format(time.gmtime()))
print('{0} локальное текущее время'.format(time.localtime()))

d = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
m = ['', 'янв', 'фев', 'мар', 'апр', 'май',
     'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
t = time.gmtime()
print('{0} {1} {2} {3} {4}:{5}:{6}\n{7}.{8}.{9}'.
      format(d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5], t[2], t[1], t[0]))

# time.sleep(5)   # sleep 5sec
print('\n')

print(time.strftime('%d.%m.%Y', time.localtime()))
print(time.strftime('%m.%d.%Y', time.localtime()))

print(time.strptime('11.07.2017', '%d.%m.%Y'))

print('\n')

import datetime

print(datetime.timedelta(milliseconds=1))
print(datetime.timedelta(minutes=1))
d = datetime.timedelta(days=1, hours=12, minutes=25)
print('days: {0}, hours: {1}, minutes: {2}'.
      format(d.days, d.seconds // 60 // 60, d.seconds // 60 % 60))

print('\n')
d1 = datetime.timedelta(days=2)
d2 = datetime.timedelta(days=7)
d3 = datetime.timedelta(weeks=1)
print('d1 = {0} days; d2 = {1} days; d3 = {2} days;'.format(d1.days, d2.days, d3.days))
print('d1 + d2 = {0}; d2 - d1 = {1}'.format((d1 + d2).days, (d2 - d1).days))
print('d1 / d2 = {0};'.format(d1 / d2))
print('d1 / 2 = {0};'.format((d1 / 2).days))
print('d1 % d2 = {0};'.format((d1 % d2).days))
print('d1 == d2 = {0}; d2 == d3 = {1};'.format(d1 == d2, d2 == d3))

print('\n')
d1 = datetime.date(2017, 12, 31)
print('date: {0}'.format(d1))
print('today {0}'.format(datetime.date.today()))
d1 = datetime.date.today()
print('year: {0}, month: {1}, day:{2}'.format(d1.year, d1.month, d1.day))
dt = datetime.timedelta(days=10)
d2 = d1 - dt
print('({0}) - {1} days = ({2})'.format(d1, dt.days, d2))
print('({0}) - ({1}) = {2} days'.format(d1, d2, (d1 - d2).days))
print('\n')
print('replace today year by 2200: ', datetime.date.today().replace(year=2200))

print('\n')
d = datetime.date.today()
print('d.m.Y = ({0}), m.d.Y = ({1})'.
      format(d.strftime('%d.%m.%Y'), d.strftime('%m.%d.%Y')))
print('weekday: {0}, isowk: {1}'.format(d.weekday(), d.isoweekday()))

print('\n')
t = datetime.time(12, 30)
print(t.strftime('%M:%H:%S'))

print('\n')
dt = datetime.datetime.today()
print('datetime today: ', dt)
print('datetime today: ', datetime.datetime.strptime('31.12.2017', '%d.%M.%Y'))
