import platform
import os
import sys
import colorama

def main():
	board = create_board()
	cur_player = "X"

	while True:
		clear_console()
		print_board(board)

		npt = sinput(f"{cur_player}: ")
		if is_valid_position(npt) and is_free_position(board, int(npt)):
			board[int(npt)] = cur_player

		if has_winner(board):
			clear_console()
			print_board(board)
			print(f"The winner is: {G + cur_player + RA}! Congratulations!")
			break

		# switching current player
		if cur_player == "X":
			cur_player = "O"
		else:
			cur_player = "X"

# =====================
# = Extra functions ===
# =====================
def create_board():
	return [i for i in range(9)]

def print_board(b):
	b = list(map(str, b)) # convert each element to string
	for i in range(len(b)):
		if b[i] == "X":
			b[i] = R + b[i] + RA
		elif b[i] == "O":
			b[i] = B + b[i] + RA

	print("+---+---+---+")
	print(f"| {b[0]} | {b[1]} | {b[2]} |")
	print("+---+---+---+")
	print(f"| {b[3]} | {b[4]} | {b[5]} |")
	print("+---+---+---+")
	print(f"| {b[6]} | {b[7]} | {b[8]} |")
	print("+---+---+---+")

def has_winner(b):
	return b[0] == b[4] == b[8] or \
			b[2] == b[4] == b[6] or \
			b[0] == b[1] == b[2] or \
			b[3] == b[4] == b[5] or \
			b[6] == b[7] == b[8] or \
			b[0] == b[3] == b[6] or \
			b[1] == b[4] == b[7] or \
			b[2] == b[5] == b[8]

if platform.system().lower() == "windows":
	def clear_console():
		os.system("cls")
else:
	def clear_console():
		os.system("clear")

def sinput(ps):
	try:
		npt = input(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		sys.exit()

def is_valid_position(pos):
	"""
	:param pos: str
	:return: bool
	"""
	try:
		pos = int(pos)
		if (pos < 0) or (pos > 8):
			return False
		return True
	except ValueError:
		return False

def is_free_position(b, pos):
	"""
	:param pos: int
	:return: bool
	"""
	if (b[pos] != "X") and (b[pos] != "O"):
		return True
	return False

if __name__ == "__main__":
	colorama.init()
	R = colorama.Fore.RED
	G = colorama.Fore.GREEN
	B = colorama.Fore.BLUE
	RA = colorama.Style.RESET_ALL
	main()
