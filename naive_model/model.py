# !/usr/bin/python
# --*--coding:utf-8--*--
# $File: model.py
# $Date: Sat Mar 19 18:08:29 2016
# $Author: Like Ma <milkpku> at <gmail>  dot <com>

import numpy as np

class state(object):
    root = None
    board = None
    untryed_move = None
    leaves = []
    visited = None

    def __init__(self, root_state=None, mv=None):
        if root_state==None:
            self.initialize()
        else:
            self.root = root_state
            self.board = self.next_state(root_state.board, mv)
            self.untryed_move = self.init_untryed_move()

        self.visited = 1

    def initialize(self, start_map=None, start_player=None):
        pass

    def init_untryed_move(self):
        pass

    def next_state(self):
        '''
        notice to perform deep copy
        '''
        pass

    # UTC value
    @property
    def value(self):
        pass

