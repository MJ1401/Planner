import unittest

from pyhop_anytime import pyhop
from pyhop_anytime.pyhop import TaskList

def travel(state, start, end):
    if start in state.places and end in state.places and start in state.at_plane:
        state.at_plane.discard(start)
        state.at_plane.add(end)
        return state

def load(state, c, loc):
    if c in state.cargo and loc in state.at_plane and (c, loc) in state.at:
        state.on_board.add(c)
        state.at.discard((c, loc))
        return state

def unload(state, c, loc):
    if c in state.cargo and loc in state.places and c in state.on_board and loc in state.at_plane:
        state.at.add((c, loc))
        state.on_board.discard(c)
        return state