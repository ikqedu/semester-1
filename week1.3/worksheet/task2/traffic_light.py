"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name:
"""

states = {"red": 4, "red_amber": 3, "green": 5, "amber": 3}

maxtime = int(input())  # read an integer number of steps (>0)


# Simulate the traffic light system up to time=maxtime in 1-second steps


def output_states(colour_timings: dict[str, int], maxtime: int) -> None:
    """Print time and state from 0 to maxtime (inclusive)."""

    if not colour_timings:
        raise ValueError("Colour timings must be passed in.")

    if maxtime < 0:
        raise ValueError("Maxtime must be >= 0")

    # Since Python 3.7+, this should construct deterministically
    # Cheap, does not need good memory scaling bc small, fixed state set
    colours = list(colour_timings)
    colour_ptr = 0
    colour_count = len(colour_timings)
    cur_colour = colours[colour_ptr]

    colour_rem_time = colour_timings[cur_colour]
    for systime in range(maxtime + 1):
        print(f"Time {systime:03} State {cur_colour}")
        colour_rem_time -= 1

        if colour_rem_time < 1:
            # Do mod operation in ptr instead of access
            # to prevent (theoretical) state_ptr overflow
            colour_ptr = (colour_ptr + 1) % colour_count
            cur_colour = colours[colour_ptr]
            colour_rem_time = colour_timings[cur_colour]


output_states(states, maxtime)

# At the end of each step you should output the time and state using the statement on line 14
