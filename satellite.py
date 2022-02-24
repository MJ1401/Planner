def calibrate(state, s, i, d):
    print("Calibration Tests")
    print((i,s) in state.on_board)
    print((i,d) in state.calibration_target)
    print((s,d) in state.pointing)
    print(i in state.power_on)
    print("Calibration Tests")
    if (i,s) in state.on_board and (i,d) in state.calibration_target and (s,d) in state.pointing and i in state.power_on:
        state.calibrated.add(i)
        return state


def switch_off(state, i, s):
    if (i,s) in state.on_board and i in state.power_on:
        state.power_on.discard(i)
        state.power_avail.add(s)
        return state


def switch_on(state, i, s):
    print("*******************************")
    print((i,s) in state.on_board)
    print(s in state.power_avail)
    print("*******************************")
    if (i,s) in state.on_board and s in state.power_avail:
        state.power_on.add(i)
        state.calibrated.discard(i)
        state.power_avail.discard(s)
        return state


def take_image(state, s, d, i, m):
    #print(i in state.calibrated)
    #print((i,s) in state.on_board)
    #print((i,m) in state.supports)
    #print(i in state.power_on)
    #print((s,d) in state.pointing)
    #print(i in state.power_on)
    if i in state.calibrated and (i,s) in state.on_board and (i,m) in state.supports and i in state.power_on and (s,d) in state.pointing and i in state.power_on:
        state.have_image.add((d,m))
        return state

# s = satellite, d_new = new direction to look, d_prev = direction it is currently looking in
def turn_to(state, s, d_new, d_prev):
    #print((s,d_prev) in state.pointing)
    #print(d_new != d_prev)
    if (s,d_prev) in state.pointing and d_new != d_prev:
        state.pointing.add((s,d_new))
        state.pointing.discard((s,d_prev))
        return state


