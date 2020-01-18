def printboard(board):
	print()
	print("+---+---+---+")
	print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
	print("+---+---+---+")
	print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
	print("+---+---+---+")
	print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
	print("+---+---+---+")

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
		user_input = input(cur_player + " move: ")

if __name__ == "__main__":
	main()
