
class stack(object):
	def __init__(self):
		self.item = []
		self.length = 0
	
	def len(self):
		return self.length
		
	def insert_item(self, k):
		self.item.insert(0,k)
		self.length+=1
	
	def remove_item(self, j):
		if self.length == 0:
			raise IndexError('stack has no item')
		else:
			self.length-=1
			return self.item.pop(self.length)

def can_move(x,y,z):
	if y.length==0 or z.length==0:
		return True
	elif x(x.length)<y(y.length) and x(x.length)<z(y.length):
		return True
	else:
		return False

def move(a, b):
	b.insert_item(a.remove_item)

def solve_towers_of_hanoi(a, b, c):
	n = a.len()
	move_num = 0
	while not a.len()==0:
		if a.len()%2 == 0:
			move(a,b)
			while not c.len()== 0:
				k=0
				while can_move(c,a,b) and k==0:
					if c.length%2 == 0 and not direction == (c,a):
						move(c,a)
					elif not direction == (c,b):
						move(c,b)
					else:
						k=1
				
		else:
			move(a,c)
			while not b.len() == 0:
				while can_move(b,a,c):
					if b.length%2 == 0:
						move(b,a)
					else:
						move(b,c)
	print('end')


	
a = stack()
b = stack()
c = stack()

n = int(input("Please give the number n:"))
for i in range(n):
	a.insert_item(i+1)

solve_towers_of_hanoi(a, b, c)
	