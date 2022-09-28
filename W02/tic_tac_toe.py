# Garren Diab
# W02 Prove
# CSE 210 - Programming with Classes

# Create lists to store the blocks that each player has played
player1 = []
player2 = []


def main():
    while True:
        try:
            # Get the grid size from the user
            grid_size = int(input(
                "Enter an odd number for the size of the grid you would like to play (e.g. 3 = 3x3, 5 = 5x5): "))
            # Check that the grid size is an odd number
            if grid_size % 2 != 0 and grid_size >= 3:
                break
            else:
                print(f"Please enter an odd number.")
        # If any other than a number is entered
        except (ValueError):
            print(f"Please enter an odd number.")
            continue

    # Calculate the max number of rounds based on the grid size
    max_rounds = grid_size**2
    # Initialize the number of rounds played
    rounds_played = 1

    # Initialize a string with the current grid
    play_grid, win_condition = draw_grid(grid_size)
    # Display the current grid
    print(play_grid)

    # Set which player's turn it is
    player = 1

    # Start the game
    while True:
        try:
            # Get the block number to change
            block = int(
                input(f"Player {player}: enter the number of the block you want to play in: "))
        # If any other than a number is entered
        except (ValueError):
            print(f"Please enter a valid block number.")
            continue

        # Capture the output of the current turn
        current_play = turn(player, play_grid, block)

        # If there was an issue with the current turn play would be False
        if current_play == "played":
            # Display that the block is taken
            print("That block as already been played.")
        else:
            # Set the new grid and continue to the next player's turn
            play_grid = current_play
            # Display the new grid
            print(play_grid)

            # Get the current game status
            game_over = winner(win_condition, grid_size)

            # Check if there is no winner
            # Continue the game
            if game_over == False:
                # If the number of rounds played is less than the max number of rounds
                if rounds_played < max_rounds:
                    # If it was player 1's turn
                    if player == 1:
                        # Make it player 2's turn
                        player = 2
                    else:
                        # Else make it player 1's turn'
                        player = 1

                    # Increase the rounds played
                    rounds_played += 1
                else:
                    print("Its a tie!")
                    break

            else:
                print(f"Congratulations: {game_over}!")
                break


def draw_grid(grid_size):
    """ Function to draw the grid.\n
    Parameters:
        grid_size: The number of blocks to draw (width and height).
    Return:
        A string containg the full grid, with numbers in each block.
    """
    # Initialize the a string to store the grid
    grid = ""
    win_condition = []
    # Current block position
    pos = 1
    # Loop for the rows
    for i in range(grid_size):
        # List to store all the postions for each row
        row = []
        # List to store all the postions for each column
        column = []
        # List to store all the postions for the first diagonal
        diag1 = []
        # List to store all the postions for the second diagonal
        diag2 = []

        # Loop for the columns
        for j in range(grid_size):
            # If the current column postion is the same as the grid size
            # Then the current postion is the final column
            if j == grid_size-1:
                # Don't add a '|' and end the line
                grid += f"{pos:2}\n"
            else:
                # Else add a '|' and continue the line
                grid += f"{pos:2}|"

            # Add the current position to the row list
            row.append(pos)
            # Using a general number pattern formula, calculate and add
            #  the relative column position
            column.append((j+1)*grid_size-i)
            #  the relative first diagonal position
            diag1.append((j+1)*(grid_size+1)-grid_size)
            #  the relative second diagonal position
            diag2.append((j+1)*(grid_size-1)+1)

            # Increase the current block postion
            pos += 1
        # Add the row list to the win_condition list
        win_condition.append(row)
        # Add the column list to the win_condition list
        win_condition.append(column)

        # After the row of blocks is completed
        # Create a row to vertially separate the blocks
        # If the current row postion is the less than the grid size
        if i < grid_size-1:
            # Loop for the columns
            for j in range(grid_size):
                # If the current column postion is the same as the grid size
                # Then the current postion is the final column
                if j == grid_size-1:
                    # Don't add a '+' and end line
                    grid += "--\n"
                else:
                    # Else add a '+' and continue the line
                    grid += "--+"
    # Add the diag1 list to the win_condition list
    win_condition.append(diag1)
    # Add the diag2 list to the win_condition list
    win_condition.append(diag2)

    # Return the string containing the grid and the win_condition list
    return grid, win_condition


def turn(player, grid, position):
    """ Takes the given position and changes it to the relevant symbol.\n
    Parameters:
        player: The current player (1 or 2).
        grid: The string containg the current grid.
        position: The number in the block that the player would \
            like to place their symbol in.
    Return:
        A string containg the new grid.
    """

    # If the given position is not in the grid string
    # This means that the chosen block has already been played
    try:
        # Get the position of the block number in the grid string
        grid_pos = grid.index(str(position))

        # If it's player 1's turn
        if player == 1:
            # Set the symbol to an "X"
            symbol = "X"
            player1.append(position)
        else:
            # Else set the symbol to an "O"
            symbol = "O"
            player2.append(position)

        # If the given position is more than 1 digit
        if len(str(position)) > 1:
            # Add a whitespace before the symbol
            symbol = f" {symbol}"
            # Increase the starting position of the substring after replacing the number
            after_pos = 2
        else:
            # Set the starting position of the substring to immediately after the symbol
            after_pos = 1
        # Change that number to the relevant symbol
        new_grid = f"{grid[0:grid_pos]}{symbol}{grid[grid_pos+after_pos:len(grid)]}"
        # Return the new grid string
        return new_grid

    except (ValueError):
        # Return "played" for error handling in the main function
        return "played"


def winner(win_condition, grid_size):
    """ Check if a row, column or diagonal has been completed by a player. 
    """
    # Iterate through the win_condition list
    for row in win_condition:
        # Number of winning positions for both players
        win_token1 = 0
        win_token2 = 0
        # Iterate through each list in the win_condition list
        for pos in row:
            # Check is the current number is in either player lists
            if pos in player1:
                # If so increase the number of winning tokens
                win_token1 += 1
            elif pos in player2:
                # If so increase the number of winning tokens
                win_token2 += 1

        # If player 1 has enough winning tokens
        if win_token1 >= grid_size:
            # Make player 1 the winner
            return "Player 1"
        # Else if player 2 has enough winning tokens
        elif win_token2 >= grid_size:
            # Make player 2 the winner
            return "Player 2"
        # Else there is no winner
        else:
            continue
    return False


if __name__ == '__main__':
    main()
