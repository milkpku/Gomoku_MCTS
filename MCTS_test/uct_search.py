# UCT search framework implement
import numpy as np
import math
from random import shuffle

class State:

  # initial from start state
  def __init__(self):
    pass

  #initial from prev state and its action
  def __init__(self, s, a):
    pass

  def moves(self):
    pass

  def is_terminal(self):
    pass

  def terminal_reward(self):
    pass

  def playout(self):
    pass

class Node:

  def __init__(self, state, father):
    self._state = state                         # state this node represent
    self._terminal = state.is_terminal()
    self._unexplored = shuffle(state.moves())   # unexplored actions
    self._father = father                       # father node, None if this is root
    self._children = dict()                     # dictionary, map action to next node
    self._N_visit = 0                           # number of visit
    self._reward = np.array([0, 0])             # reward for two players

    if (father):
      self._player = 1 - father._player
    else:
      self._player = 0

# uct search framework
# input root node v0, select leaf node in search tree and then playout, backup
# returned result along tree
# finally return the best child 
def uct_search(v0):
  t = True
  while (t):
    vl = tree_policy(v0)
    delta = default_policy(vl)
    backup(vl, delta)

  return best_child(v0, 0)

def tree_policy(v):
  while (not v._terminal):
    if (v._unexplored):
      return expand(v)
    else:
      v = best_child(v, Cp)
  return v

"""
  expand given node by chose randomly from its untried actions, instance a node
  to be its child, then return the child back
  
  Inputs:
    v   MCT node
  
  Outputs:
    vc  newly instanced child of v
"""
def expand(v):
  action = v._unexplored.pop()
  vc = Node(State(v.state, action), v)
  v._children.append(vc)  
  return vc

def best_child(v, C):
  # UCT choice policy
  max_r = -1
  best_vc = v._children[0]

  for vc in v._children:
    r = (vc.reward[v._player] / vc._N_visit
      + C * math.sqrt( 2 * math.log(v._N_visit) / vc._N_visit ) )

    if (r > max_r):
      max_r = r
      best_vc = vc

  return best_vc

def default_policy(v):
  return v._state.playout()

def backup(v, delta):
  while (v):
    v._reward += delta
    v._N_visit += 1
    v = v._father

if __name__=="__main__":
    print("hello world")