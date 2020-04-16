def result(arr):
	temp = []
	temp1 = []

	# check for rows
	for i in range(3):
		if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2]:
			temp.append(arr[i][0])

	if len(temp) >= 2:
		return "Impossible"
	elif len(temp) != 0 and temp[0] == ('X', 'O'):
		return temp[0] + " wins"

	# check for columns
	for j in range(3):
		if arr[0][j] == arr[1][j] and arr[1][j] == arr[2][j]:
			temp1.append(arr[0][j])

	if len(temp1) >= 2:
		return "Impossible"
	elif len(temp1) != 0 and temp1[0] == ('X', 'O'):
		return temp1[0] + " wins"

	empty_list = []
	for i in arr:
		for j in i:
			if j == "_" or j == " ":
				empty_list.append(j)

	# check for diagonals
	if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and (arr[2][2] == 'X' or arr[2][2] == 'O'):
		return arr[0][0] + " wins"

	if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and (arr[2][0] == 'X' or arr[2][0] == 'O'):
		return arr[0][2] + " wins"

	if count_O(symbols) + count_X(symbols) == 9:
		return "Draw"


def count_X(array):
	count = 0
	for i in array:
		for j in i:
			if j == "X":
				count += 1
	return count


def count_O(array):
	count = 0
	for i in array:
		for j in i:
			if j == "O":
				count += 1
	return count


def while_func(char):
	global empty
	global symbols
	inp = input('Enter the Coordinates:').split(" ")
	if len(inp) == 2:
		y = int(inp[0])
		x = int(inp[1])
		if x > 3 or y > 3 or x < 1 or y < 1:
			print("Coordinates should be from 1 to 3!")

		elif symbols[abs(x - 3)][abs(y - 1)] == " ":
			symbols[abs(x - 3)][abs(y - 1)] = char
			print('---------')
			for i in range(3):
				print('|', end=" ")
				for j in range(3):
					print(symbols[i][j], end=" ")
				print('|')
			print('---------')

		else:
			print("This cell is occupied! Choose another one!")
		if result(symbols):
			if result(symbols).startswith('X') or result(symbols).startswith('O') or result(symbols).startswith('D'):
				print(result(symbols))
				empty = False
				return empty


# Driver Code

symbols = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print('---------')
for i in range(3):
	print('|', end=" ")
	for j in range(3):
		print(symbols[i][j], end=" ")
	print('|')
print('---------')

empty = True  # Flag
count = 0
while (empty):
	count += 1
	if count % 2 == 0:
		while_func('O')
	elif count % 2 == 1:
		while_func('X')
	else:
		print("You should enter numbers!")
