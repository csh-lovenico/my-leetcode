import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Initial case: if we start at target, no need to take any bus
        if source == target:
            return 0

        # Create adj_graph which stores possibilities to go from a route
        adj_graph = collections.defaultdict(set)

        # Stop_map stores all the buses that visit a route
        stop_map = collections.defaultdict(set)

        # Iterate through list
        for bus, route in enumerate(routes):
            n = len(route)

            # Create edge between adjacent routes & add bus to the routes
            for i in range(n - 1):
                adj_graph[(bus, route[i])].add(route[i + 1])
                stop_map[route[i]].add(bus)

            # Create edge between start & end route
            adj_graph[(bus, route[n - 1])].add(route[0])

            # Add bus to end route
            stop_map[route[n - 1]].add(bus)

            # Convert this route list into a set
            routes[bus] = set(route)

        # Set min to inf and initialize visited set
        min_buses = float("inf")
        visited = set()

        # Queue would contain all bus routes with source as stop
        this_q = collections.deque([(1, b, source) for b in range(len(routes)) if (b, source) in adj_graph])

        # Continue while queue is not empty
        while this_q:
            # Get number of current buses, current bus name, current stop
            num_buses, cur_bus, cur_stop = this_q.popleft()

            # If cur_stop is the target stop or target stop is in the same bus route, then return
            if cur_stop == target or target in routes[cur_bus]:
                min_buses = min(min_buses, num_buses)
                continue

            # Add route to visited
            visited.add((cur_bus, cur_stop))

            # If current num_buses is greater than found min, then do not continue
            if num_buses >= min_buses:
                continue

            # Get all buses that visit the stop
            buses_in_stop = stop_map[cur_stop]

            # For each bus in the stop
            for next_bus in buses_in_stop:
                # Iterate through all adjacent route
                for adj_route in adj_graph[(next_bus, cur_stop)]:
                    # Check if visited (no repeated computations)
                    if (next_bus, adj_route) in visited:
                        continue

                    # Increment number of buses if next_bus != cur_bus
                    next_num_buses = num_buses + 1 if next_bus != cur_bus else num_buses
                    this_q.append((next_num_buses, next_bus, adj_route))

        # Return min if not inf else -1
        return min_buses if min_buses != float("inf") else -1
    