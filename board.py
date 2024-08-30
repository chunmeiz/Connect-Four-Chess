class Board:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.board = [['.' for _ in range(cols)] for _ in range(rows)]
  #self.board is a list of list

  # Load a specific board state
  def load_board(self, rows):
    # rows is a 2D list of strings containing the board state
    self.board = [list(row) for row in rows]

  # Check if a move is valid by verifying if the top row of the selected column is empty
  def is_valid_move(self, col):
    if self.board[0][col] == '.':
      return True
    else:
      return False
    

  # Get the next open row in a column for a piece to be dropped
  def get_next_open_row(self, col):
    for row in range(len(self.board)-1,-1,-1):
      if self.board[row][col] == '.':
        return row
    return None

  # Drop a piece into the board at the specified column
  def drop_piece(self, col, piece):
    row = self.get_next_open_row(col)
    #you must use self to call the function in an object
    if row is not None:
      self.board[row][col] = piece


  # Check if the specified piece player has won the game
  def check_win(self, piece):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])-3):
        if self.board[i][j] == piece and self.board[i][j+1] == piece and self.board[i][j+2] == piece and self.board[i][j+3] == piece:
          return True
    for j in range(len(self.board[0])):
      for i in range(len(self.board)-3):
        if self.board[i][j] == piece and self.board[i+1][j] == piece and self.board[i+2][j] == piece and self.board[i+3][j] == piece:
          return True
    for i in range(len(self.board)-3):
      for j in range(len(self.board[i])-3):
        if self.board[i][j] == piece and self.board[i+1][j+1] == piece and self.board[i+2][j+2] == piece and self.board[i+3][j+3] == piece:
          return True
    for i in range(len(self.board)-3):
      for j in range(3,len(self.board[i])):
        if self.board[i][j] == piece and self.board[i+1][j-1] == piece and self.board[i+2][j-2] == piece and self.board[i+3][j-3] == piece:
          return True
    return False
  
  # Check if the board is full
  def is_full(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == '.':
          return False
    return True

  # Print the current state of the board
  def print_board(self):
    print("| " + " ".join(str(i) for i in range(self.cols)) + " |")
    for row in self.board:
      print("| " + " ".join(row) + " |")
    print("| " + "-" * (self.cols * 2 - 1) + " |")