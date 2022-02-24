from pyhop_anytime import *
global state, goals
state = State('state')
state.at = Oset([('sand', 'usa'), ('bananas', 'uk'), ('snow', 'brazil'), ('oranges', 'russia'), ('peaches', 'egypt')])
state.at_plane = Oset(['usa'])
state.cargo = Oset(['bananas', 'sand', 'peaches', 'snow', 'oranges'])
state.places = Oset(['usa','uk', 'brazil', 'russia', 'egypt'])
state.on_board = Oset()

goals = State('goals')
goals.at = Oset([('bananas','brazil'),('sand','egypt'),('snow','russia'),('oranges','uk'),('peaches','usa')])