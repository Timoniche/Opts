from best_neighbor import BestNeighbor
from hill_climbing import swap


def get_neighbors_without_tabu(
        route,
        tabu_map,
        iteration,
):
    best_neighbor = None
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            if iteration >= tabu_map[i][j]:
                neighbor = route.copy()
                swap(neighbor, i, j)
                neighbors.append(neighbor)

                if not best_neighbor:
                    best_neighbor = BestNeighbor(neighbor, i, j)
                else:
                    best_neighbor.update(neighbor, i, j)

    return neighbors, best_neighbor


def run_tabu_search(
        initial_route,
        num_cities,
        max_iterations,
        tabu_jump,
):
    best_dist = 1e9
    tabu_map = [[0] * num_cities for _ in range(num_cities)]

    current_route = initial_route

    iteration = 1
    while iteration <= max_iterations:
        neighbors, best_neighbor = get_neighbors_without_tabu(
            route=current_route,
            tabu_map=tabu_map,
            iteration=iteration,
        )
        if not neighbors:
            iteration += 1
            continue

        current_route, current_distance = best_neighbor.route, best_neighbor.dist
        best_dist = min(best_dist, float(best_neighbor.dist))
        tabu_map[best_neighbor.i][best_neighbor.j] = iteration + tabu_jump
        print(f'ts distance {current_distance}, best_dist {best_dist}, it: {iteration}')
        iteration += 1

    return current_route, best_dist
