import numpy as np
import random


def calculate_distance(route):
    route_extended = np.append(route, [route[0]], axis=0)
    return np.sum(np.sqrt(np.sum(np.diff(route_extended, axis=0) ** 2, axis=1)))


class BestNeighbor:
    def __init__(
            self,
            route,
            i,
            j
    ):
        self.route = route
        self.i = i
        self.j = j
        self.dist = calculate_distance(self.route)

    def update(self, next_route, i, j):
        next_dist = calculate_distance(next_route)
        if next_dist < self.dist:
            self.route = next_route
            self.i = i
            self.j = j
            self.dist = next_dist


def create_initial_route(cities):
    return np.array(random.sample(list(cities), len(cities)))


def get_neighbors(route):
    best_neighbor = None
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

            if not best_neighbor:
                best_neighbor = BestNeighbor(neighbor, i, j)
            else:
                best_neighbor.update(neighbor, i, j)

    return neighbors, best_neighbor


def hill_climbing(initial_route):
    current_route = initial_route
    current_distance = calculate_distance(current_route)

    it = 1
    while True:
        neighbors, best_neighbor = get_neighbors(current_route)
        next_distance = best_neighbor.dist

        if next_distance >= current_distance:
            break

        current_route, current_distance = best_neighbor.route, next_distance
        print(f'hc distance {current_distance}, it: {it}')
        it += 1

    return current_route, current_distance


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
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
                # tabu_map[i][j] = iteration + tabu_jump

                if not best_neighbor:
                    best_neighbor = BestNeighbor(neighbor, i, j)
                else:
                    best_neighbor.update(neighbor, i, j)

    return neighbors, best_neighbor


def tabu_search(
        initial_route,
        max_iterations=100,
):
    num_cities = len(initial_route)
    tabu_map = [[0] * num_cities] * num_cities

    current_route = initial_route
    current_distance = calculate_distance(current_route)

    it = 1
    while it <= max_iterations:
        neighbors, best_neighbor = get_neighbors_without_tabu(
            route=current_route,
            tabu_map=tabu_map,
            iteration=it,
        )
        if not neighbors:
            it += 1
            continue

        current_route, current_distance = best_neighbor.route, best_neighbor.dist
        print(f'ts distance {current_distance}, it: {it}')
        it += 1

    return current_route, current_distance


def main():
    np.random.seed(42)
    random.seed(42)

    num_cities = 10
    cities = np.random.rand(num_cities, 2)
    initial_route = create_initial_route(cities)

    hc_route, hc_distance = hill_climbing(initial_route)
    print('\n\n\n')
    ts_route, ts_distance = tabu_search(initial_route)


if __name__ == '__main__':
    main()

# hc distance 4.454390156115023, it: 1
# hc distance 3.429802482264245, it: 2
# hc distance 2.6740947589495168, it: 3
# hc distance 2.010989834586995, it: 4
# hc distance 1.6438732062490133, it: 5
# hc distance 1.455618486250753, it: 6
# hc distance 1.383174632379454, it: 7
