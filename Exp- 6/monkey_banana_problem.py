from collections import deque

initial_state = (0, 0, False, False)
goal_state = (2, 2, True, True)

def get_successors(state):
    successors = []
    monkey_position, box_position, monkey_on_box, has_bananas = state
    
    if has_bananas:
        return successors
    
    for new_position in range(3):
        if new_position != monkey_position:
            successors.append((new_position, box_position, False, False))
    
    if not monkey_on_box:
        for new_position in range(3):
            if new_position != box_position and new_position == monkey_position:
                successors.append((new_position, new_position, False, False))
    
    if monkey_position == box_position and not monkey_on_box:
        successors.append((monkey_position, box_position, True, False))
    
    if monkey_position == box_position and monkey_on_box and monkey_position == goal_state[0]:
        successors.append((monkey_position, box_position, True, True))
    
    return successors

def monkey_banana_problem(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, actions = queue.popleft()
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        if current_state == goal_state:
            return actions
        
        for successor in get_successors(current_state):
            queue.append((successor, actions + [successor]))
    
    return None

solution = monkey_banana_problem(initial_state, goal_state)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
