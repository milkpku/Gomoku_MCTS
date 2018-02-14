from uct_search import State 
import numpy as np
from copy import deepcopy
from random import randint

class Tic_Tac_Toe(State):

  _board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
  _players = ['x', 'o']
  _player_id = 0
  _moves = [(0, 0), (0, 1), (0, 2), 
            (1, 0), (1, 1), (1, 2), 
            (2, 0), (2, 1), (2, 2)]
  _is_terminal = False
  _reward = np.array([0, 0])

  def __init__(self, s = None, a = None):
    
    if (not s):
      return

    self._board = deepcopy(s._board)
    self._player_id = 1 - s._player_id

    row, col = a
    stone = self._players[s._player_id]
    self._board[row][col] = stone

    self._moves = []
    for i in range(3):
      for j in range(3):
        if (self._board[i][j] == "-"):
          self._moves.append((i, j))

    # exame if terminate
    _b = self._board
    if ( _b[row][0] == _b[row][1] and _b[row][1] == _b[row][2]):
      self._is_terminal = True

    if ( _b[0][col] == _b[1][col] and _b[1][col] == _b[2][col]):
      self._is_terminal = True

    if (row == col and _b[0][0] == _b[1][1] and _b[1][1] == _b[2][2]):
      self._is_terminal = True

    if (row + col == 2 and _b[0][2] == _b[1][1] and _b[1][1] == _b[2][0]):
      self._is_terminal = True

    if (self._is_terminal):
      self._reward[self._player_id] = -1
      self._reward[s._player_id] = 1

    if (len(self._moves) == 0 and not self._is_terminal):
      self._is_terminal = True

  # standard output of board
  def __str__(self):
    output = ''
    for line in self._board:
      output += '\n' + line[0] + ' ' + line[1] + ' ' + line[2]
    return output

  __repr__ = __str__

  def moves(self):
    return self._moves

  def is_terminal(self):
    return self._is_terminal

  def terminal_reward(self):
    return self._reward

  def playout(self):
    tmp = self

    while (not tmp.is_terminal()):
      pick = randint(0, len(tmp._moves)-1)
      tmp = Tic_Tac_Toe(tmp, tmp._moves[pick]) 

    return tmp
      
if __name__=="__main__":
  from IPython import embed; embed()