from os import system

#TODO: ADD COLORAMA
def printboard(board):
	system("cls") # windows' clear console
	print("+---+---+---+")
	print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
	print("+---+---+---+")
	print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
	print("+---+---+---+")
	print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
	print("+---+---+---+")

def checkwinner(board):
	#diagonal
	if board[0] == board[4] == board[8]: return True
	elif board[2] == board[4] == board[6]: return True
	#horizontal
	elif board[0] == board[1] == board[2]: return True
	elif board[3] == board[4] == board[5]: return True
	elif board[6] == board[7] == board[8]: return True
	#vertical
	elif board[0] == board[3] == board[6]: return True
	elif board[1] == board[4] == board[7]: return True
	elif board[2] == board[5] == board[8]: return True

	return False

def main():
	board = [
		"0", "1", "2",
		"3", "4", "5",
		"6", "7", "8"
	]
	winner = None
	cur_player = "X"

	run = True
	while run:
		printboard(board)
		try:
			user_input = int(input(cur_player + " move: "))
		except ValueError:
			continue
		except KeyboardInterrupt:
			run = False
		# Validating user input
		if user_input < 0 or user_input > 8:
			print("No such slot")
			continue

		# check that the slot is not busy
		if board[user_input] == "X" or board[user_input] == "O":
			continue

		board[user_input] = cur_player
		winner = checkwinner(board)
		if winner:
			printboard(board)
			print("Winner is %s!" % cur_player)
			break
		
		if cur_player == "X": cur_player = "O"
		else: cur_player = "X"

if __name__ == "__main__":
	main()
