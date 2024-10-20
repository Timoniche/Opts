from fitness import calculate_distance


class BestNeighbor:
    def __init__(
            self,
            route,
            i,
            j
    ):
        self.route = route.copy()
        self.i = i
        self.j = j
        self.dist = calculate_distance(self.route)

    def update(self, next_route, i, j):
        next_dist = calculate_distance(next_route)
        if next_dist < self.dist:
            self.route = next_route.copy()
            self.i = i
            self.j = j
            self.dist = next_dist
