from best_neighbor import BestNeighbor
from fitness import calculate_distance


def get_neighbors(route):
    best_neighbor = None
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route.copy()
            swap(neighbor, i, j)
            neighbors.append(neighbor)

            if not best_neighbor:
                best_neighbor = BestNeighbor(neighbor, i, j)
            else:
                best_neighbor.update(neighbor, i, j)

    return neighbors, best_neighbor


def swap(neighbor, i, j):
    tmp = neighbor[i].copy()
    neighbor[i] = neighbor[j].copy()
    neighbor[j] = tmp.copy()


def run_hill_climbing(initial_route):
    current_route = initial_route
    current_distance = calculate_distance(current_route)

    iteration = 1
    while True:
        neighbors, best_neighbor = get_neighbors(current_route)
        next_distance = best_neighbor.dist

        if next_distance >= current_distance:
            break

        current_route, current_distance = best_neighbor.route.copy(), next_distance
        print(f'hc distance {current_distance}, it: {iteration}')
        iteration += 1

    return current_route, current_distance
