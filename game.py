from os import system
import sys
import platform

SYSTEM = platform.system()

def clearconsole():
	if SYSTEM == "Windows":
		system("cls")
	else:
		system("clear")

def printboard(b):
	system("cls") # windows' clear console
	print("+---+---+---+")
	print(f"| {b[0]} | {b[1]} | {b[2]} |")
	print("+---+---+---+")
	print(f"| {b[3]} | {b[4]} | {b[5]} |")
	print("+---+---+---+")
	print(f"| {b[6]} | {b[7]} | {b[8]} |")
	print("+---+---+---+")

def checkwinner(b):
	if b[0] == b[4] == b[8] or \
		b[2] == b[4] == b[6] or \
		b[0] == b[1] == b[2] or \
		b[3] == b[4] == b[5] or \
		b[6] == b[7] == b[8] or \
		b[0] == b[3] == b[6] or \
		b[1] == b[4] == b[7] or \
		b[2] == b[8] == b[8]:
		return True
	return False

def main():
	board = [str(i) for i in range(9)]
	winner = None
	curr_player = "X"

	while True:
		printboard(board)
		try:
			user_input = int(input(f"{curr_player} plays: "))
		except ValueError:
			continue
		except (KeyboardInterrupt, EOFError):
			sys.exit()
			
		# if user_input slot not exists
		if (user_input < 0) or (user_input > 8):
			print("No such slot")
			continue

		# check that the slot is not busy
		if (board[user_input] == "X") or (board[user_input] == "O"):
			continue

		board[user_input] = curr_player
		winner = checkwinner(board)
		if winner:
			printboard(board)
			print(f"Winner is {curr_player}!")
			break
		
		if curr_player == "X":
			curr_player = "O"
		else:
			curr_player = "X"

if __name__ == "__main__":
	main()
