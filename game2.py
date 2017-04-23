#!/usr/bin/python

# Given a starting position [x,y] (0<x,y<9), 
# initial direction faced (W, S, N, E) on 8 x 8 square board 
# and the target position, direction and maximum actions allowed, 
# print all possible actions robot can make to get to that position.

N = 0
E = 1
S = 2
W = 3

BOUNDARY = 8

MAX_NUM_ACTIONS_ALLOWED = 0

INT_FACE = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
FACE_INT = {'N': 0, 'E': 1, 'S': 2, 'W': 3}


class Node:
	def __init__(self, x=0, y=0, dir=N):
		self.x = x
		self.y = y
		self.dir = dir

		self.prev = None
		self.act = None
		self.level = 0

	def equal(self, node):
		return self.x == node.x and self.y == node.y and self.dir == node.dir

	# for debugging purpose
	def print_me(self):
		print str(self.x) + str(self.y) + str(self.dir)		


def move_allowed(node):
	if node.dir == N:
		return node.y < BOUNDARY
	elif node.dir == E:
		return node.x < BOUNDARY
	elif node.dir == S:
		return node.y > 1
	else:
		return node.x > 1

def move_forward(node):
	next_node = Node(node.x, node.y, node.dir)

	next_node.prev = node
	next_node.act = 'M'
	next_node.level = node.level + 1

	if node.dir == N:
		next_node.y += 1
	elif node.dir == E:
		next_node.x += 1
	elif node.dir == S:
		next_node.y -= 1
	else:
		next_node.x -= 1

	return next_node 

def turn_left(node):
	next_node = Node(node.x, node.y, node.dir)

	next_node.prev = node
	next_node.act = 'L'
	next_node.level = node.level + 1

	if node.dir == N:
		next_node.dir = W
	else:
		next_node.dir -= 1

	return next_node

def turn_right(node):
	next_node = Node(node.x, node.y, node.dir)

	next_node.prev = node
	next_node.act = 'R'
	next_node.level = node.level + 1

	if node.dir == W:
		next_node.dir = N
	else:
		next_node.dir += 1

	return next_node

def get_actions(node, actions):
	if node.prev.prev != None:
		get_actions(node.prev, actions)
	actions.append(node.act)

def print_actions(actions, num):
	out = 'Actions - ' + str(num) + ' : '
	for i in range(len(actions)):
		out += str(actions[i])
		if i != len(actions)-1:
			out += ','
	print out

def user_prompt(node, sstr):
	location = raw_input(sstr+' position (please use comma to separate x and y): ')
	cord = []
	while True:
		for d in location.split(','):
			if d.isdigit():
				cord.append(int(d))
		if len(cord) == 2 and cord[0]*cord[1] > 0 \
			and cord[0] <= BOUNDARY and cord[1] <= BOUNDARY:
			break
		else:
			print 'invalid input for position, please retry'
			location = raw_input(sstr+' position: ')
			cord = []

	direction = raw_input(sstr+' direction faced (valid direction: N or E or S or W): ')
	faced = N
	while True:
		faced = direction.upper()
		if not FACE_INT.has_key(direction.upper()):
			print 'invalid input for direction, please retry'
			direction = raw_input(sstr+' direction faced: ')
		else:
			faced = FACE_INT[direction.upper()]
			break

	node.x = cord[0]
	node.y = cord[1]
	node.dir = faced


def main():
	original = Node()
	target = Node()

	user_prompt(original, 'Original')
	user_prompt(target, 'Target')
	d = raw_input('Maximum actions allowed (positive integer only): ')
	while True:
		if d.isdigit():
			MAX_NUM_ACTIONS_ALLOWED = int(d)
			break
		else:
			print 'invalid input, please retry'
			d = raw_input('Maximum actions allowed: ')

	queue = [original]
	level = 0
	num = 0

	while len(queue):
		curr = queue.pop(0)
		if curr.equal(target) and curr.level <= MAX_NUM_ACTIONS_ALLOWED:
			actions = []
			get_actions(curr, actions)
			num += 1
			print_actions(actions, num)

		if curr.level < MAX_NUM_ACTIONS_ALLOWED:
			if move_allowed(curr):
				queue.append(move_forward(curr))
			queue.append(turn_left(curr))
			queue.append(turn_right(curr))

	if num == 0:
		print 'No possible actions!'
	else:
		print 'No more possible actions!'


if __name__ == '__main__':
	main()


