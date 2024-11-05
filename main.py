goalState = {'A': '0', 'B': '0', 'C': '0', 'D': '0', 'E': '0'}
cost = 0
roomStates = {'A': '0', 'B': '0', 'C': '0', 'D': '0', 'E': '0'}

# Initial input
print("Enter the starting location of vacuum (A/B/C/D/E) = ")
location = input().strip()
print()

# Get room states from user
for room in roomStates:
    action = input(f"Enter the state of {room} (0 for clean / 1 for dirty): ")
    roomStates[room] = action

# General Outputs
print()
print(f"\nCurrent State: {roomStates}")
print(f"\nGoal state: {goalState}")
print(f"\nVacuum is placed in location {location}\n")

def clean_room(room):
    global cost
    if roomStates[room] == '1':  # If dirty
        roomStates[room] = '0'
        cost += 1
        print(f"Location {room} was dirty\nLocation {room} has been cleaned\nCost for cleaning is 1.")
        return True
    return False

def move_to_room(from_room, to_room):
    global cost
    print(f"\n{from_room} is clean")
    print(f"\n{from_room} -> {to_room}")
    print("\nCost for moving within rooms = 1")
    cost += 1

# Main logic based on starting location
if roomStates != goalState:
    # Starting logic for all locations
    if location == 'A':
        if clean_room('A'):
            if roomStates == goalState:
                print("\nGoal state has been met.")
                print(f"\nPerformance Measurement: {cost}")
        else:
            # Move to B if A is clean
            move_to_room('A', 'B')
            if clean_room('B'):
                if roomStates == goalState:
                    print("\nGoal state has been met.")
                    print(f"\nPerformance Measurement: {cost}")
            else:
                # Move to C if B is clean
                move_to_room('B', 'C')
                if clean_room('C'):
                    if roomStates == goalState:
                        print("\nGoal state has been met.")
                        print(f"\nPerformance Measurement: {cost}")
                else:
                    # Move to D if C is clean
                    move_to_room('C', 'D')
                    if clean_room('D'):
                        if roomStates == goalState:
                            print("\nGoal state has been met.")
                            print(f"\nPerformance Measurement: {cost}")
                    else:
                        # Move to E if D is clean
                        move_to_room('D', 'E')
                        if clean_room('E'):
                            if roomStates == goalState:
                                print("\nGoal state has been met.")
                                print(f"\nPerformance Measurement: {cost}")

    elif location == 'B':
        if clean_room('B'):
            if roomStates == goalState:
                print("\nGoal state has been met.")
                print(f"\nPerformance Measurement: {cost}")
        else:
            move_to_room('B', 'A')
            if clean_room('A'):
                if roomStates == goalState:
                    print("\nGoal state has been met.")
                    print(f"\nPerformance Measurement: {cost}")
            else:
                move_to_room('A', 'C')
                if clean_room('C'):
                    if roomStates == goalState:
                        print("\nGoal state has been met.")
                        print(f"\nPerformance Measurement: {cost}")
                else:
                    move_to_room('C', 'D')
                    if clean_room('D'):
                        if roomStates == goalState:
                            print("\nGoal state has been met.")
                            print(f"\nPerformance Measurement: {cost}")
                    else:
                        move_to_room('D', 'E')
                        if clean_room('E'):
                            if roomStates == goalState:
                                print("\nGoal state has been met.")
                                print(f"\nPerformance Measurement: {cost}")

    elif location == 'C':
        if clean_room('C'):
            if roomStates == goalState:
                print("\nGoal state has been met.")
                print(f"\nPerformance Measurement: {cost}")
        else:
            move_to_room('C', 'B')
            if clean_room('B'):
                if roomStates == goalState:
                    print("\nGoal state has been met.")
                    print(f"\nPerformance Measurement: {cost}")
            else:
                move_to_room('B', 'A')
                if clean_room('A'):
                    if roomStates == goalState:
                        print("\nGoal state has been met.")
                        print(f"\nPerformance Measurement: {cost}")
                else:
                    move_to_room('A', 'D')
                    if clean_room('D'):
                        if roomStates == goalState:
                            print("\nGoal state has been met.")
                            print(f"\nPerformance Measurement: {cost}")
                    else:
                        move_to_room('D', 'E')
                        if clean_room('E'):
                            if roomStates == goalState:
                                print("\nGoal state has been met.")
                                print(f"\nPerformance Measurement: {cost}")

    elif location == 'D':
        if clean_room('D'):
            if roomStates == goalState:
                print("\nGoal state has been met.")
                print(f"\nPerformance Measurement: {cost}")
        else:
            move_to_room('D', 'C')
            if clean_room('C'):
                if roomStates == goalState:
                    print("\nGoal state has been met.")
                    print(f"\nPerformance Measurement: {cost}")
            else:
                move_to_room('C', 'B')
                if clean_room('B'):
                    if roomStates == goalState:
                        print("\nGoal state has been met.")
                        print(f"\nPerformance Measurement: {cost}")
                else:
                    move_to_room('B', 'A')
                    if clean_room('A'):
                        if roomStates == goalState:
                            print("\nGoal state has been met.")
                            print(f"\nPerformance Measurement: {cost}")
                    else:
                        move_to_room('A', 'E')
                        if clean_room('E'):
                            if roomStates == goalState:
                                print("\nGoal state has been met.")
                                print(f"\nPerformance Measurement: {cost}")

    elif location == 'E':
        if clean_room('E'):
            if roomStates == goalState:
                print("\nGoal state has been met.")
                print(f"\nPerformance Measurement: {cost}")
        else:
            move_to_room('E', 'D')
            if clean_room('D'):
                if roomStates == goalState:
                    print("\nGoal state has been met.")
                    print(f"\nPerformance Measurement: {cost}")
            else:
                move_to_room('D', 'C')
                if clean_room('C'):
                    if roomStates == goalState:
                        print("\nGoal state has been met.")
                        print(f"\nPerformance Measurement: {cost}")
                else:
                    move_to_room('C', 'B')
                    if clean_room('B'):
                        if roomStates == goalState:
                            print("\nGoal state has been met.")
                            print(f"\nPerformance Measurement: {cost}")
                    else:
                        move_to_room('B', 'A')
                        if clean_room('A'):
                            if roomStates == goalState:
                                print("\nGoal state has been met.")
                                print(f"\nPerformance Measurement: {cost}")
