from datetime import date
today = date.today()
today_weekday = date.weekday(today)
"""
Print Today. If you want find 3 days after, input p 3. 7 days before, input n 7.
"""

Month=['Null', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Weekday=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
leapyear=[]
month30=[4,6,9,11]
month31=[1,3,5,7,8,10,12]
class DAY(object):
	def __init__(self, year, month, day, weekday):
		self._year = year
		self._month = month
		self._day = day
		self._weekday = weekday
	def __str__(self):
		return '%d-%s-%d %s' % (self._year, Month[self._month], self._day, Weekday[self._weekday])
	
main = DAY(today.year, today.month, today.day,today_weekday)

print(today.day)
def months_day(day):
	if day._month in month30:
		return 30
	elif day._month in month31:
		return 31
	elif day._month == 2:
		if day._year in leapyear:
			return 29
		else:
			return 28
def make_leapyear():
	global leapyear
	for i in range(9999):
		if i%400==0:
			leapyear.append(i)
		elif i%100!=0 and i%4==0:
			leapyear.append(i)

def check_input(d):
	if d=="x":
		print("bye")
		return True	
	else:
		a = d.split(' ')
		if a[0] == 'p' or a[0] == 'n':
			try:
				b = int(a[1])
			except:
				return False
			return True
		else:
			return False
def plus_day(day, x):
	day._day+=x
	while months_day(day) < day._day:
		day._day-=months_day(day)
		if day._month == 12:
			day._month = 1
			day._year +=1
		else:
			day._month += 1
	print(day)
	
def minus_day(day, x):
	day._day-=x
	day._day
	while day._day <= 0:
		if day._month == 1:
			day._month = 12
			day._year -=1
		else:
			day._month -= 1
		day._day+=months_day(day)
	print(day)
	
print(main)
make_leapyear()
while True:
	d=str(input("If you want Find after dd days, input p dd. before n days, input n dd."))
	d2=d[2:]
	if not check_input(d):
		print("please enter proper words.")
	elif d=='x':
		break
	elif d[0]=='p':
		plus_day(main, int(d2))
	elif d[0]=='n':
		minus_day(main, int(d2))
	else:
		break