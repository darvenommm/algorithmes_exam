# Норм обьяснение https://youtu.be/S2eVYez_j58?si=5hmjrnvmX7tGAkAF&t=4149

def max_cost(capacity: int, weights: list[int], costs: list[int]) -> int:
    if len(weights) != len(costs):
        raise ValueError('Weights is not equal with costs!')

    things_count: int = len(weights)
    cache: list[list[int]] = [
        [0 for _ in range(capacity + 1)]
        for _ in range(things_count + 1)
    ]

    for thing_index in range(things_count):
        for capacity_value in range(1, capacity + 1):
            if capacity_value < weights[thing_index]:
                cache[thing_index + 1][capacity_value] = cache[thing_index][capacity_value]
            else:
                new_value: int = max(
                    cache[thing_index][capacity_value],
                    costs[thing_index] + cache[thing_index][capacity_value - weights[thing_index]]
                )
                cache[thing_index + 1][capacity_value] = new_value\

    return cache[-1][-1]

# result: int = max_cost(
#     13,
#     [3, 4, 5, 8, 9],
#     [1, 6, 4, 7, 6],
# )
# print(result)

# result1: int = max_cost(
#     12,
#     [7, 3, 1, 5, 4],
#     [10, 4, 2, 6, 7],
# )
# print(result1)
