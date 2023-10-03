katz_deli = []

# Function to show everyone their current place in line
def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        for position, person in enumerate(deli_line, start=1):
            current_line += f" {position}. {person}"
        print(current_line)

def take_a_number(deli_line, name):
    deli_line.append(name)
    position = len(deli_line)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving = deli_line.pop(0)
        print(f"Currently serving {serving}.")