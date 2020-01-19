
def printboard(board):
	print()
	print("+---+---+---+")
	print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
	print("+---+---+---+")
	print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
	print("+---+---+---+")
	print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
	print("+---+---+---+")

# def checkwinner(board, player):
# 	#diagonal
# 	if board[0] == board[]

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

		board[user_input] = cur_player
		if cur_player == "X": cur_player = "O"
		else: cur_player = "X"
		# winner = checkwinner(board, cur_player) 


if __name__ == "__main__":
	main()
