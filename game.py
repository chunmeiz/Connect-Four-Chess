from board import Board

class Game:
  def __init__(self, players, rows=6, cols=7, save_file=None):
    if len(players) < 2:
      raise ValueError("At least two players are required.")
    self.players = players
    self.current_player_index = 0
    self.rows = rows
    self.cols = cols
    self.board = Board(self.rows, self.cols)
    #print(self.board)
    # Load the game state from a file if one is provided
    if save_file is not None:
      with open(save_file, "r") as f:
        player_index = f.readline()
        try:
          self.current_player_index = int(player_index)
        except ValueError:
          raise ValueError(f"Player index in save file is not an integer: {player_index}")
        # Validate the player index is within bounds
        if self.current_player_index < 0 or self.current_player_index >= len(self.players):
          raise ValueError(f"Player index in save file is out of bounds: {self.current_player_index}")
        save_rows = f.read().strip().split("\n")
        # Validate that the save game has the correct number of rows and
        # columns
        if len(save_rows) != self.rows:
          raise ValueError("Invalid save file. Number of rows does not match the board.")
        if not all(len(row) == self.cols for row in save_rows):
          raise ValueError("Invalid save file. Number of columns does not match the board.")
        # Validate that the save game only contains spaces and valid pieces
        valid_pieces = [player.piece for player in self.players] + ["."]
        for c in "".join(save_rows):
          if c not in valid_pieces:
            raise ValueError(f"Invalid character found in save file: '{c}'")
        self.board.load_board(save_rows)
  
  def get_current_player(self):
    return self.players[self.current_player_index]

  def switch_player(self):
    self.current_player_index = (self.current_player_index + 1) % len(self.players)

  def play(self):
    while True:
      self.board.print_board()
      current_player = self.get_current_player()
      print(f"{current_player.name}'s turn.")

      col = int(input("Enter the column (0-6) to drop your piece: "))
      while not self.board.is_valid_move(col):
        print("Invalid move. Try again.")
        col = int(input("Enter the column (0-6) to drop your piece: "))
      self.board.drop_piece(col, self.get_current_player().piece)
      if self.board.check_win(self.get_current_player().piece):
        print(f"{current_player.name} wins!")
        break
      elif self.board.is_full():
        print("It's a tie!")
        break
      self.switch_player()
    self.board.print_board()
