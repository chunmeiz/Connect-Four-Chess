from board import Board
from game import Game
from player import Player

if __name__ == "__main__":
  # Run your tests in this block
  players = [Player("Player 1", "X"), Player("Player 2", "O")]
  # Change the save_file to None to start a game from the beginning
  #game = Game(players)
  game = Game(players, save_file="save1.txt")

  # Instead of playing the game, you may wish to print out
  # attributes or the result of methods from the game.board
  # object while testing your code.

  game.play()