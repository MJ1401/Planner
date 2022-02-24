from satellite import *
from pyhop_anytime import *
# To install pyhop_anytime: pip3 install git+https://github.com/gjf2a/pyhop_anytime


# Every pyhop planner should have a method named start which sets up the initial task list from the goals
def start(state, goals):
    images_not_taken = [(image, tool)
                   for image, tool in goals.have_image
                   if (image, tool) not in state.have_image]
    if len(images_not_taken) == 0:
        return TaskList(completed=True)
    else:
        return TaskList([('choose_picture', images_not_taken), ('start', goals)])

## WRITE ADDITIONAL METHODS HERE ##

def choose_picture(state, images_not_taken):
    tasks = []
    for image, tool in images_not_taken:
        tasks.append([('choose_sat', image, tool)])
    return TaskList(tasks)

def choose_sat(state, image, tool):
    tasks = []
    for ins, tool2 in state.supports:
        if tool2 == tool:
            for ins2, sat in state.on_board:
                if ins == ins2:
                    tasks.append([('get_sat_ready', sat, image, tool, ins)])
    return TaskList(tasks)

def get_sat_ready(state, sat, image, tool, ins):
    tasks = []
    #if sat in state.power_avail:
        #tasks.append([('switch_on', ins, sat)])
    tasks.append(('switch_on', ins, sat))
    #if ins not in state.power_on:
        #tasks.append([('switch_on', ins, sat)])
    for ins2, dest in state.calibration_target:
        if ins2 == ins:
            for sat2, dest_curr in state.pointing:
                if sat2 == sat and dest != dest_curr:
                    tasks.append(('turn_to', sat, dest, dest_curr))
                    tasks.append(('calibrate', sat, ins, dest))
                    break
            break
    tasks.append(('ready_for_image', sat, image, tool, ins))
    return TaskList(tasks)

def ready_for_image(state, sat, image, tool, ins):
    tasks = []
    for sat2, dest in state.pointing:
        if sat == sat2 and dest != image:
            tasks.append(('turn_to', sat, image, dest))
            break
    #if (image, tool) not in state.have_image:
    #    tasks.append([('take_image', sat, image, ins, tool)])
    #    tasks.append([('switch_off', ins, sat)])
    tasks.append(('take_image', sat, image, ins, tool))
    tasks.append(('switch_off', ins, sat))
    return TaskList(tasks)


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods(start, choose_picture, choose_sat, get_sat_ready, ready_for_image) # Include all other methods you write as parameters
    return planner


if __name__ == '__main__':
    anyhop_main(make_satellite_planner())