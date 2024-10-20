import numpy as np
import random

from hill_climbing import run_hill_climbing
from tabu_search import run_tabu_search


def create_initial_route(cities):
    return np.array(random.sample(list(cities), len(cities)))


def main():
    np.random.seed(42)
    random.seed(42)

    num_cities = 15
    cities = np.random.rand(num_cities, 2)
    initial_route = create_initial_route(cities)

    _, hc_distance = run_hill_climbing(initial_route)
    print('\n\n\n')
    _, ts_distance = run_tabu_search(
        initial_route,
        num_cities,
        max_iterations=1000,
        tabu_jump=20,
    )

    print(f'Best Hill Climbing distance: {hc_distance}')
    print(f'Best Tabu Search distance: {ts_distance}')


if __name__ == '__main__':
    main()
