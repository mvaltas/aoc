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
        (loops, remainder) = divmod(position + (OP[direction] * clicks), dial)

        # backwards rotation
        if direction == 'L':
            through_zero += abs(loops)
            # corrections...
            if position == 0 and remainder > 0:
                through_zero -= 1
            elif position > 0 and remainder == 0:
                through_zero += 1 
        # forward rotarion
        else:
            through_zero += loops

        position = remainder
                
        if position == 0:
            on_zero += 1

print(f"on_zero:{on_zero}, past:{through_zero}")
