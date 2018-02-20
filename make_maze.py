from random import shuffle, randrange

w = 10
h = 6
vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
					  # N, E, S, W
matrix_adiacency =  [ [ [0, 0, 0, 0] for i in range(w) ] for j in range(h) ]


entry_x = 0
start_x = 0
entry_y = 0
start_y = 0
exit_y = w-1
exit_x = h-1
exist_exit = True
# print exit_x , exit_y

def make_maze():
 
	def walk(x, y):
		vis[y][x] = 1
 
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)
		for (xx, yy) in d:
			if vis[yy][xx]: continue
			if xx == x: hor[max(y, yy)][x] = "+  "
			if yy == y: ver[y][max(x, xx)] = "   "
			walk(xx, yy)
 
	walk(randrange(w), randrange(h))
	# out_maze = open('output', 'w')
	for (a, b) in zip(hor, ver):
		print ''.join(a + ['\n'] + b)
		# out_maze.write(''.join(a + ['\n'] + b)+'\n')
	# out_maze.close()

make_maze()

def escape_from_maze(entry_x, entry_y, exit_x, exit_y):
	global ver
	global hor
	global matrix_adiacency
	global start_x
	global start_y
	global exist_exit

	set_neighborhood(start_x, start_y)

	#print 'neighborhood [',matrix_adiacency[start_x][start_y][0], ',' ,matrix_adiacency[start_x][start_y][1], ',' ,matrix_adiacency[start_x][start_y][2], ',' ,matrix_adiacency[start_x][start_y][3], ']'

	while ( start_x!=exit_x or start_y!=exit_y ):

		# print '\n'
		if (0 in matrix_adiacency[start_x][start_y]):
			index = matrix_adiacency[start_x][start_y].index(0)
			#print 'index ',index
			set_entry_point(index, -1)
		elif ( -1 in matrix_adiacency[start_x][start_y]):
			index = matrix_adiacency[start_x][start_y].index(-1)
			#print 'index ',index
			set_entry_point(index, 1)
		else:
			exist_exit = False

	if(exist_exit):
		print 'Path find (showed as exit --> entry) from entry point: [',entry_x,'][',entry_y,'] to exit point: [',exit_x,'][',exit_y,']'
		while ( not (start_x==entry_x and start_y==entry_y) ):
			print '[',start_x,'][',start_y,'] -> ',
			index = matrix_adiacency[start_x][start_y].index(-1)
			#print 'index ',index
			set_entry_point(index, 1)
		print '[',entry_x,',' ,entry_y,']'
	else:
		print 'Cannot find exit.'

def set_entry_point(indx, value):
	global matrix_adiacency
	global start_x
	global start_y

	if(indx==0):
		# will go to north
		start_x -= 1 
		# set south of the new entry point as backward
		matrix_adiacency[start_x][start_y][2] = value	
		#print 'Go to start_x: ',start_x,' start_y: ',start_y,' value: ',value		
	elif (indx==1):
		# will go to east
		start_y += 1
		# set west of the new entry point as backward
		matrix_adiacency[start_x][start_y][3] = value
		#print 'Go to start_x: ',start_x,' start_y: ',start_y,' value: ',value
	elif (indx==2):
		# will go to south
		start_x += 1
		# set north of the new entry point as backward
		matrix_adiacency[start_x][start_y][0] = value
		#print 'Go to start_x: ',start_x,' start_y: ',start_y,' value: ',value
	elif (indx==3):
		# will go to west
		start_y -= 1
		# set east of the new entry point as backward
		matrix_adiacency[start_x][start_y][1] = value
		#print 'Go to start_x: ',start_x,' start_y: ',start_y,' value: ',value
	set_neighborhood(start_x, start_y)
	#print 'neighborhood [',matrix_adiacency[start_x][start_y][0], ',' ,matrix_adiacency[start_x][start_y][1], ',' ,matrix_adiacency[start_x][start_y][2], ',' ,matrix_adiacency[start_x][start_y][3], ']'


def set_neighborhood(x, y):
	global ver
	global hor
	global matrix_adiacency
	global start_x
	global start_y

	if (hor[x][y]=='+--'):
		# wall at north
		matrix_adiacency[x][y][0] = 1
	if (hor[x+1][y]=='+--'):
		# wall at south
		matrix_adiacency[x][y][2] = 1
	if (ver[x][y]=='|  '):
		# wall at west
		matrix_adiacency[x][y][3] = 1
	if (ver[x][y+1]=='|  ' or ver[x][y+1]=='|'):
		# wall at east
		matrix_adiacency[x][y][1] = 1	

escape_from_maze(entry_x, entry_y, exit_x, exit_y)

