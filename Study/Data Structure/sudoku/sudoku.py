from tree import *

def solveSudoku2by2(a):
	check(a)
	r_i, c_i = 0, 0
	while(a[r_i][c_i]!=0): # find start point
		if((r_i,c_i)==(3,3)):
			print("Already Solved")
			return a
		r_i = r_i+(c_i+1)//4
		c_i = (c_i+1)%4	
	tree = STree(SNode(a,0))
	tree.expand_tree(r_i,c_i,tree.root)
	return tree.dfs_tree(tree.root)
	
def check(sudoku):
	if(len(sudoku) != 4): # check column size
		raise SyntaxError("Invalid input!")
	for row in sudoku: # check row size
		if(len(row) != 4):
			raise SyntaxError("Invalid input!")
	for row in sudoku:
		for element in row:
			if(element and row.count(element)>1):
				raise SyntaxError("Invalid input!")
	for i in range(4):
		col = [sudoku[0][i], sudoku[1][i], sudoku[2][i], sudoku[3][i]]
		for element in col:
			if(element and col.count(element)>1):
					raise SyntaxError("Invalid input!")
	for i in range(2):
		for j in range(2):
			square = [sudoku[2*i][2*j], sudoku[2*i][2*j+1], sudoku[2*i+1][2*j], sudoku[2*i+1][2*j+1]]
			for element in square:
				if(element and square.count(element)>1):
					raise SyntaxError("Invalid input!")


if __name__ == '__main__':
	a = [[0, 2, 1, 3], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
	# a = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 2, 3, 1], [0, 0, 0, 0]]
	# a = [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 2, 1], [2, 1, 3, 4]]
	# a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(solveSudoku2by2(a))