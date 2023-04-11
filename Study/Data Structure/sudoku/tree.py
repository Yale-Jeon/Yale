import copy

class SNode(object):
	"""A node for Sudoku representation"""
	def __init__(self, sudoku, depth):
		self.sstate = sudoku
		self.depth = depth
		self.nchildren = 0
		self.children = [None for i in range(4)]
		
	def find_insert(self, r_i, c_i):
		"""find values which could be inserted"""
		if(self.sstate[r_i][c_i]==0):
			num_list = [1,2,3,4] # list of number possible to be inserted
			for i in range(2): # check 2 by 2 square
				for j in range(2):
					if((self.sstate[r_i//2*2+i][c_i//2*2+j] in num_list)):
						num_list.remove(self.sstate[r_i//2*2+i][c_i//2*2+j])
			for i in range(4): # check row and column
				if(self.sstate[r_i][i] in num_list):
					num_list.remove(self.sstate[r_i][i])
				if(self.sstate[i][c_i] in num_list):
					num_list.remove(self.sstate[i][c_i])		
			return num_list
		else:
			return None
	
	def print_node(self):
		"""print the node"""
		print(self.depth,self.sstate)

class STree(object):
	"""A tree presentation to solve sudoku"""
	def __init__(self, rootnode):
		"""create an empty tree"""
		self.root = rootnode
	
	def insert_node(self, i, sudokunode, parent):
		"""attach the new node to parent's i-th child"""
		parent.children[i-1] = sudokunode
	
	def expand_tree(self, r_i, c_i, curroot):
		"""expand the tree if found a number"""
		if(r_i>3 or c_i>3):
			return
		val_list = curroot.find_insert(r_i,c_i) # list of values possible to be inserted
		if(val_list):
			curroot.nchildren = len(val_list)
			for num in val_list:
				tmp = copy.deepcopy(curroot.sstate)
				tmp[r_i][c_i] = num
				curchild = SNode(tmp, curroot.depth+1)
				self.insert_node(num, curchild, curroot)
			r_i = r_i+(c_i+1)//4
			c_i = (c_i+1)%4
			for child in curroot.children:
				if(child):
					self.expand_tree(r_i, c_i, child)
		else:
			if(curroot.sstate[r_i][c_i]==0):
				return
			r_i = r_i+(c_i+1)//4
			c_i = (c_i+1)%4			
			self.expand_tree(r_i,c_i,curroot)
	
	def dfs_tree(self, subtree):
		"""visit the tree and try to find a solution and output"""
		if(subtree.nchildren != 0): # if not leaf node
			subtree.print_node()
			for child in subtree.children:
				if(child):
					rlt = self.dfs_tree(child)
					if(rlt): # if rlt != None
						return rlt
			if(subtree.depth==0): # if all rlt == None
				return "Impossible"
		else: # if leaf node
			for row in subtree.sstate:
				for i in row:
					if(i==0):
						subtree.print_node()
						return None
			print("Solved")
			return subtree.sstate
