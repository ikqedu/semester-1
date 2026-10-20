"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name:
"""

states = {"red": 4, "red_amber": 3, "green": 5, "amber": 3}

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

# Simulate the traffic light system up to time=maxtime in 1-second steps

# 15 for this example
total_light_time = sum(states.values())

# for tstep until maxtime:
# if tstep is in category of colour:
# print state

"""
while systime < maxtime:
    loop through states:
        increment systime
        output

while systime < maxtime:
    create new rem time dict
        look at colour n:
            output colour nk until colour n's rem time < 1
            next colour
    
"""

# Since Python 3.7+, this should construct deterministically
# Cheap, does not need good memory scaling bc small, fixed state set
colours = list(states.keys())
state_ptr = 0
state_count = len(states)

# maxtime + 1 because maxtime is not # of timesteps
while systime < maxtime + 1:
    # Reset state, rem time
    state = colours[state_ptr]
    state_rem_time = states[state]

    # Dual call is suboptimal
    while state_rem_time > 0 and systime < maxtime + 1:
        print(f"Time {systime:03} State {state}")
        state_rem_time -= 1
        systime += 1

    state_ptr = (state_ptr + 1) % state_count

# At the end of each step you should output the time and state using the statement on line 14
