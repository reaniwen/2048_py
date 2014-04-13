Board= [[0]*4 for row in range(4)]
def print_board(Board):
	for row in Board:
		for cell in row:
			print cell,
		print
	print

def judge_dir(drt):
	#if drt == "some direction":
	#	init two pointers, 
	#	the space pointer point to the first zero position
	#	the second potinter equal to the space pointer
	#	move sec ptr to the first value positon
	#	move value to space, space+1
	#	sec move to the next value position
	if drt == 'w':
		for col in range(4):
			space = 0
			while space != 3 and Board[space][col] !=0:
				space += 1 #init space
			row = space
			while row != 4:
				if Board[row][col]!=0:
					Board[space][col] = Board[row][col]
					if space != row:
						Board[row][col] = 0
					space += 1
				row += 1

	elif drt == 's':
		for col in range(4):
			space = 3
			while space != 0 and Board[space][col] != 0:
				space -= 1
			row = space
			while row != -1:
				if Board[row][col]!=0:
					Board[space][col] = Board[row][col]
					if space != row:
						Board[row][col] = 0
					space -= 1
				row -= 1

	elif drt == 'a':
		for row in range (4):
			space = 0
			while space != 3 and Board[row][space] !=0:
				space +=1 #init space
			col = space
			while col != 4:
				if Board[row][col]!=0:
					Board[row][space] = Board[row][col]
					if space != col:
						Board[row][col] = 0
					space += 1
				col += 1

	elif drt == 'd':
		for row in range(4):
			space = 3
			while space != 0 and Board[row][space] !=0:
				space +=1
			col = space
			while col != -1:
				if Board[row][col] !=0:
					Board[row][space] = Board[row][col]
					if space !=col:
						Board[row][col] = 0
					space -=1
				col -=1


def chkwin(): #check whether we win

def chkmove():

					

print_board(Board)
#i = input('How many:')
x,y = input('location:')
Board[x][y]= 1
print_board(Board)
while True:
	drt = raw_input("direction:")
	judge_dir(drt)
	print_board(Board)
	x,y = input('location:')
	Board[x][y]= 1
	print_board(Board)
