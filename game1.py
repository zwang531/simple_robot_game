#!/usr/bin/python

N = 0
E = 1
S = 2
W = 3
BOUNDARY = 8
INT_FACE = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
FACE_INT = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

class Robot:
	def __init__(self, x=0, y=0, dir=N):
		self.x = x
		self.y = y
		self.dir = dir

	def move(self, actions):
		for act in actions:
			if act == 'M':
				if self.dir == N: 
					if self.y < BOUNDARY-1:
						self.y += 1
				elif self.dir == E: 
					if self.x < BOUNDARY-1:
						self.x += 1
				elif self.dir == S: 
					if self.y > 0:
						self.y -= 1
				else: 
					if self.x > 0:
						self.x -= 1
			elif act == 'L':
				if self.dir == N:
					self.dir = W
				else:
					self.dir -= 1
			else:
				if self.dir == W:
					self.dir = N
				else:
					self.dir += 1


def main():
	location = raw_input('Location (please use comma to separate x and y): ')
	cord = []
	while True:
		for d in location.split(','):
			if d.isdigit():
				cord.append(int(d))
		if len(cord) == 2 and cord[0]*cord[1] >= 0 \
			and cord[0] < BOUNDARY and cord[1] < BOUNDARY:
			break
		else:
			print 'invalid input for location, please retry'
			location = raw_input('Location: ')
			cord = []

	direction = raw_input('Direction faced (valid direction: N or E or S or W): ')
	faced = N
	while True:
		faced = direction.upper()
		if not FACE_INT.has_key(direction.upper()):
			print 'invalid input for direction, please retry'
			direction = raw_input('Direction faced: ')
		else:
			faced = FACE_INT[direction.upper()]
			break

	moves = raw_input('Actions (valid action: M or L or R, please use comma to separate actions): ') 
	actions = []
	while True:
		err = False
		for move in moves.split(','):
			act = move.upper()
			if act != 'M' and act != 'L' and act != 'R':
				print 'invalid input for actions, please retry'
				moves = raw_input('Actions: ') 
				actions = []
				err = True
				break
			actions.append(act)
		if err == False:
			break

	robot = Robot(cord[0], cord[1], faced)
	robot.move(actions)

	print '[' + str(robot.x) + ',' + str(robot.y) + '],',
	print INT_FACE[robot.dir]

if __name__ == '__main__':
	main()


