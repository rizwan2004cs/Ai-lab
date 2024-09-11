import itertools

def calculate_route_cost(route, distance_matrix):
    """Calculate the total cost of a given route."""
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance_matrix[route[i]][route[i + 1]]
    total_cost += distance_matrix[route[-1]][route[0]]  # Return to start
    return total_cost

def tsp_brute_force(distance_matrix):
    """Solve the Traveling Salesman Problem using brute force."""
    n = len(distance_matrix)
    cities = list(range(n))
    min_cost = float('inf')
    best_route = []

    # Generate all possible routes
    for route in itertools.permutations(cities):
        current_cost = calculate_route_cost(route, distance_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = route

    return best_route, min_cost

# Example distance matrix for 4 cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_cost = tsp_brute_force(distance_matrix)

print("Best Route:", best_route)
print("Minimum Cost:", min_cost)
