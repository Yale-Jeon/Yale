#import unittest

class stack(object):
	def __init__(self,name):
		self.item = []
		self.length = 0
		self.name = name

	def len(self):
		return self.length
	
	def first(self):
		if self.length == 0:
			return 0
		else:
			return self.item[-1]
		
	def insert_item(self, k):
		print('Insert', k, 'to', self.name)
		self.item.append(k)
		self.length += 1
	
	def remove_item(self):
		if self.length == 0:
			raise IndexError('stack has no item')
		else:
			self.length -= 1
			item = self.item[-1]
			self.item = self.item[:-1]
			return item

"""	
def move_other():
	global a, b, c
	if a.first() == 1:
		if b.first() > c.first():
			move(c,b)
		else:
			move(b,c)
	elif b.first() == 1:
		if a.first() > c.first():
			move(c,a)
		else:
			move(a,c)
	else:
		if b.first() > a.first():
			move(a,b)
		else:
			move(b,a)
"""

class Hanoi:
	def __init__(self, a, b, c, n):
		self.a = a
		self.b = b
		self.c = c
		self.n = n
		self.num = 0

	def move(self, a, b):
		print('move', a.item, b.item)
		if a.len() > 0:
			b.insert_item(a.remove_item)
			print(a.name + '->' + b.name, b.item)

	def move_right(self, a, b, c):
		print('move_rigth', a.item, b.item, c.item)
		if a.first() == 1:
			self.move(a, b)
		elif b.first() == 1:
			self.move(b, c)
		else:
			self.move(c, a)

	def move_left(self, a, b, c):
		print('move_left', a.item, b.item, c.item)
		if a.first() == 1:
			self.move(a, c)
		elif b.first() == 1:
			self.move(b, a)
		else:
			self.move(c, b)

	def solve_towers_of_hanoi(self):
		if self.a.len()%2 == 0:
			while not self.a.len() == 0:
				if self.num%2 == 1:
					self.move_right(self.a,self.b,self.c)
				else:
					if self.a.first() == 1:
						if self.b.first() > self.c.first():
							self.move(self.c,self.b)
						else:
							self.move(self.b,self.c)
					elif self.b.first() == 1:
						if self.a.first() > self.c.first():
							self.move(self.c,self.a)
						else:
							self.move(self.a,self.c)
					else:
						if self.b.first() > self.a.first():
							self.move(self.a,self.b)
						else:
							self.move(self.b,self.a)
				self.num+=1
		else:
			while not self.a.len() == 0:
				if self.num%2 == 1:
					self.move_left(self.a,self.b,self.c)
				else:
					if self.a.first() == 1:
						if self.b.first() > self.c.first():
							self.move(self.c,self.b)
						else:
							self.move(self.b,self.c)
					elif self.b.first() == 1:
						if self.a.first() > self.c.first():
							self.move(self.c,self.a)
						else:
							self.move(self.a,self.c)
					else:
						if self.b.first() > self.a.first():
							self.move(self.a,self.b)
						else:
							self.move(self.b,self.a)
				self.num+=1
		print(self.num)
			
a = stack('A')
b = stack('B')
c = stack('C')
n = int(input("Please give the number n:"))
for i in range(n):
	a.insert_item(n-i)

Problem = Hanoi(a, b, c, n)
Problem.solve_towers_of_hanoi()