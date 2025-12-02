import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
OP = {"R": +1, "L": -1 }

# Expected
# lands: 1132
# passthrough: 6623
position = 50
dial = 100
on_zero = 0
through_zero = 0

with open(f"{SCRIPT_DIR}/input.txt") as f:
    for l in f.readlines():
        movement = l.strip()
        (direction, clicks) = movement[0], int(movement[1:])
        # brute force dial rotation, analytical `p = abs( delta // dial)`
        # only works for full cycle, 360º loop, not for boundary crossing
        for _ in range(clicks):
            position = (position + OP[direction]) % dial
            if position == 0:
                through_zero += 1

        if position == 0:
            on_zero += 1

print(f"on_zero:{on_zero}, past:{through_zero}")
