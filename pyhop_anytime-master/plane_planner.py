from plane_example1 import *
from plane import *
from pyhop_anytime.pyhop import *

visited = []

def start(state, goals):
    undelivered = [(cargo, destination)
                   for cargo, destination in goals.at
                   if (cargo, destination) not in state.at]
    if len(undelivered) == 0:
        return TaskList(completed=True)
    else:
        return TaskList([('select', undelivered), ('start', goals)])


def select(state, undelivered):
    on_board_check = []
    for c in state.on_board:
        on_board_check.append(c)
    if len(on_board_check) != 0:
        return TaskList([('unload', state.on_board.get_first(), state.at_plane.get_first())])
    else:
        needs_moved = []
        for c, l in undelivered:
            if l in state.at_plane and (c, l) in state.at:
                return TaskList([('load', c, l), ('deliver_on_plane', c)])
            needs_moved.append(c)
        for c, l in state.at:
            if c in needs_moved:
                return TaskList([('travel', state.at_plane.get_first(), l), ('load', c, l), ('deliver_on_plane', c)])

def deliver_on_plane(state, on_board):
    going_to = state.places.get_first()
    for c, p in goals.at:
        if c in on_board:
            going_to = p
    return TaskList([('travel', state.at_plane.get_first(), going_to)])


def make_plane_planner():
    planner = Planner()
    planner.declare_operators(travel, load, unload)
    planner.declare_methods(start, select, deliver_on_plane)
    return planner


if __name__ == '__main__':
    anyhop_main(make_plane_planner())